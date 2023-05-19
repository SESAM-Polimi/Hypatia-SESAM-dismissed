# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:21:57 2023

@author: GP
"""

def _calc_regional_cost_planning(self):
    
    self.totalcost_allregions = np.zeros((len(self.model_data.settings.years), 1))
    self.inv_allregions = 0
    years = -1 * np.arange(len(self.model_data.settings.years))

    for reg in self.model_data.settings.regions:

        totalcost_regional = np.zeros((len(self.model_data.settings.years), 1))

        for ctgry in self.model_data.settings.technologies[reg].keys():

            if ctgry != "Demand":

                totalcost_regional += cp.sum(
                    self.cost_inv_tax[reg][ctgry]
                    - self.cost_inv_sub[reg][ctgry]
                    + self.cost_fix[reg][ctgry]
                    + self.cost_fix_tax[reg][ctgry]
                    - self.cost_fix_sub[reg][ctgry]
                    + self.cost_variable[reg][ctgry]
                    + self.cost_decom[reg][ctgry]
                    - self.salvage_inv[reg][ctgry],
                    axis=1,
                )

                self.inv_allregions += self.cost_inv_fvalue[reg][ctgry]

                if ctgry != "Transmission" and ctgry != "Storage":
                    for emission_type in get_emission_types(self.model_data.settings.global_settings):
                        totalcost_regional += cp.sum(
                            self.emission_cost_by_region[reg][emission_type][ctgry], axis=1
                        )
                                                
        for carr in self.unmetdemandbycarrier[reg].keys():
                        
            totalcost_regional += cp.sum(self.cost_unmet_demand[reg][carr],axis=1)

        discount_factor = (
            1 + self.model_data.regional_parameters[reg]["discount_rate"]["Annual Discount Rate"].values
        )

        totalcost_regional_discounted = cp.multiply(
            totalcost_regional, np.power(discount_factor, years)
        )
        self.totalcost_allregions += totalcost_regional_discounted

def _calc_regional_emission(self):

    self.totalemission_allregions = np.zeros((len(self.model_data.settings.years), 1))
    
    for reg in self.model_data.settings.regions:
        
        totalemission_regional = np.zeros((len(self.model_data.settings.years), 1))
        
        for emission_type in get_emission_types(self.model_data.settings.global_settings):
            
            totalemission_regional_by_type = np.zeros((len(self.model_data.settings.years), 1))
            
            for ctgry in self.model_data.settings.technologies[reg].keys():

                if ctgry != "Demand" and ctgry != "Transmission" and ctgry != "Storage":
                    
                    totalemission_regional_by_type += cp.sum(
                        self.emission_by_region[reg][emission_type][ctgry], axis=1
                    )
                    
            totalemission_regional += totalemission_regional_by_type
            
        self.totalemission_allregions += totalemission_regional
        
def _calc_regional_cost_operation(self):
    
    self.totalcost_allregions = 0
    for reg in self.model_data.settings.regions:

        totalcost_regional = 0

        for ctgry in self.model_data.settings.technologies[reg].keys():

            if ctgry != "Demand":

                totalcost_regional += cp.sum(
                    self.cost_fix[reg][ctgry]
                    + self.cost_fix_tax[reg][ctgry]
                    - self.cost_fix_sub[reg][ctgry]
                    + self.cost_variable[reg][ctgry]
                )

                if ctgry != "Transmission" and ctgry != "Storage":
                    for emission_type in get_emission_types(self.model_data.settings.global_settings):
                        totalcost_regional += cp.sum(
                            self.emission_cost_by_region[reg][emission_type][ctgry], axis=1
                        )
                        
        for carr in self.unmetdemandbycarrier[reg].keys():
                        
            totalcost_regional += cp.sum(self.cost_unmet_demand[reg][carr],axis=1)

        self.totalcost_allregions += totalcost_regional
        
def _calc_lines_cost_planning(self):
    
    years = -1 * np.arange(len(self.model_data.settings.years))
    self.totalcost_lines = np.zeros((len(self.model_data.settings.years), 1))

    for line in self.model_data.settings.lines_list:

        self.totalcost_lines += cp.sum(
            self.cost_inv_line[line]
            + self.cost_fix_line[line]
            + self.cost_decom_line[line],
            axis=1,
        )

    for reg in self.model_data.settings.regions:

        for key, value in self.cost_variable_line[reg].items():

            self.totalcost_lines += cp.sum(value, axis=1)

    discount_factor_global = (
        1
        + self.model_data.global_parameters["global_discount_rate"][
            "Annual Discount Rate"
        ].values
    )

    self.totalcost_lines_discounted = cp.multiply(
        self.totalcost_lines, np.power(discount_factor_global, years)
    )
    
def _calc_lines_cost_operation(self):

    self.totalcost_lines = 0

    for line in self.model_data.settings.lines_list:

        self.totalcost_lines += cp.sum(self.cost_fix_line[line], axis=1)

    for reg in self.model_data.settings.regions:

        for key, value in self.cost_variable_line[reg].items():

            self.totalcost_lines += cp.sum(value, axis=1)
            
def _calc_tot_cost_singlenode(self):

    if self.model_data.settings.mode == ModelMode.Planning:
        self.tot_cost_single_node = (
            cp.sum(self.totalcost_allregions) + self.inv_allregions
        )

    elif self.model_data.settings.mode == ModelMode.Operation:

        self.tot_cost_single_node = self.totalcost_allregions

def _calc_tot_cost_multinode(self):

    if self.model_data.settings.mode == ModelMode.Planning:

        self.tot_cost_multi_node = (
            cp.sum(self.totalcost_lines_discounted + self.totalcost_allregions)
            + self.inv_allregions
        )

    elif self.model_data.settings.mode == ModelMode.Operation:

        self.tot_cost_multi_node = self.totalcost_allregions + self.totalcost_lines
        
def _calc_tot_emission(self):

    if self.model_data.settings.mode == ModelMode.Planning:
        self.tot_emissions = cp.sum(self.totalemission_allregions)

    elif self.model_data.settings.mode == ModelMode.Operation:

        self.tot_emissions = cp.sum(self.totalemission_allregions)