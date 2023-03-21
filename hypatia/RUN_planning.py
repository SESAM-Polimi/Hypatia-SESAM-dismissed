# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:06:55 2023

@author: GP
"""

"""
Utopia MODEL
Planning mode
"""

from hypatia import Model
import os
from hypatia import Merge_results
from hypatia import Plotter

#%%
Utopia = Model(path="examples/Planning_teaching_hourly/sets", mode="Planning")

#%%
Utopia.create_data_excels(
    path ='examples\Planning_teaching_hourly\parameters',                      
    force_rewrite=True                                                  
)

#%%
Utopia.read_input_data("examples\Planning_teaching_hourly\parameters")

#%%
Utopia.run(solver='gurobi',verbosity=True, force_rewrite= True)

#%%
# os.mkdir("examples/Planning_teaching/results/") 
 
#%%
Utopia.to_csv(path='examples/Planning_teaching_hourly/results', force_rewrite=True, postprocessing_module="aggregated")

#%% 

# Utopia.create_config_file(
#     path = 'examples/Planning_teaching/config.xlsx'                   # Path to the config file
# )

#%%
plots = Plotter(
  results = Utopia,
  config = 'examples/Planning_teaching_hourly/config.xlsx',
  hourly_resolution = True, # if model has an hourly resultion otherwise False
)

#%% 

# os.mkdir("examples/Planning_teaching/plots/") 

#%%
plots.plot_total_capacity(
    path = 'examples/Planning_teaching_hourly/plots/totalcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
    decom_cap=True,
)

#%%
plots.plot_new_capacity(
    path = 'examples/Planning_teaching_hourly/plots/newcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
)

#%%
plots.plot_prod_by_tech(
    path = 'examples/Planning_teaching_hourly/plots/prod_by_tech.html',
    tech_group = 'Power Generation',
    kind="bar",
)

#%%
plots.plot_use_by_technology(
    path = 'examples/Planning_teaching_hourly/plots/use_by_tech.html',
    fuel_group = 'Oil',
    kind="bar",
)

#%%
plots.plot_fuel_prod_cons(
    path = 'examples/Planning_teaching_hourly/plots/prod_con_share_2020.html',
    years = ["Y0"],
    fuel_group = 'Electricity',
    trade=True,
)

plots.plot_fuel_prod_cons(
    path = 'examples/Planning_teaching_hourly/plots/prod_con_share_2030.html',
    years = ["Y10"],
    fuel_group = 'Electricity',
    trade=True,
)

#%%
plots.plot_emissions(
    path = 'examples/Planning_teaching_hourly/plots/emissions.html',
    tech_group = 'Power Generation',
    emission_type = ["CO2"],
    kind="bar",
    aggregate=True
)

#%%
plots.plot_hourly_prod_by_tech(
    path = 'examples/Planning_teaching_hourly/plots/hourlyprod_2020.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y0"],
    start="2020-01-01 00:00:00",
    end="2020-01-01 23:00:00",
)

plots.plot_hourly_prod_by_tech(
    path = 'examples/Planning_teaching_hourly/plots/hourlyprod_2030.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y10"],
    start="2030-01-01 00:00:00",
    end="2030-01-01 23:00:00",
)

#%%
plots.plot_regional_costs(
    path = 'examples/Planning_teaching_hourly/plots/regionalcosts_bytechs.html',
    stacked_by = 'techs'
)
