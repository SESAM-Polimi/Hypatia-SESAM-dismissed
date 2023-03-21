# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:57:56 2023

@author: GP
"""

"""
Utopia MODEL
Operation mode
"""

from hypatia import Model
import os
from hypatia import Merge_results
from hypatia import Plotter
#%%
Utopia = Model(path="examples/Operation_teaching/sets", mode="Operation")

#%%
# Utopia.create_data_excels(
#     path ='examples\Operation_teaching\parameters',                      
#     force_rewrite=True                                                  
# )

#%%
Utopia.read_input_data("examples\Operation_teaching\parameters")

#%%
Utopia.run(solver='gurobi',verbosity=True, force_rewrite= True)

#%%
# os.mkdir("examples/Operation_teaching/results/") 
 
#%%
Utopia.to_csv(path='examples/Operation_teaching/results', force_rewrite=True, postprocessing_module="aggregated")

#%%
# Utopia.create_config_file(path = 'examples/Operation_teaching/config.xlsx')

#%%
plots = Plotter(
  results = Utopia,
  config = 'examples/Operation_teaching/config.xlsx',
  hourly_resolution = True, # if model has an hourly resultion otherwise False
)

#%%
# os.mkdir("examples/Operation_teaching/plots/") 
 
#%%
plots.plot_total_capacity(
    path = 'examples/Operation_teaching/plots/totalcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
    decom_cap=True,
    aggregate=False
)

#%%
plots.plot_prod_by_tech(
    path = 'examples/Operation_teaching/plots/prod_by_tech.html',
    tech_group = 'Power Generation',
    kind="bar",
    aggregate=False
)

#%%
plots.plot_use_by_technology(
    path = 'examples/Operation_teaching/plots/use_by_tech_ng.html',
    fuel_group = 'Natural Gas',
    kind="bar",
)

#%%
plots.plot_fuel_prod_cons(
    path = 'examples/Operation_teaching/plots/prod_con_share.html',
    years = ["Y0"],
    fuel_group = 'Electricity',
    trade=True
)

#%%
plots.plot_emissions(
    path = 'examples/Operation_teaching/plots/emissions.html',
    tech_group = 'Power Generation',
    emission_type = ["CO2 emissions"],
    kind="bar",
    aggregate=False
)

#%%
plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation_teaching/plots/hourlyprod_1.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "area",
    year = ["Y0"],
    start="2020-01-01 00:00:00",
    end="2020-01-01 23:00:00",
    aggregate=False
)
#%%
plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation_teaching/plots/hourlyprod_2.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y0"],
    start="2020-12-09 00:00:00",
    end="2020-12-11 23:00:00",
    aggregate=False
)

#%%
plots.plot_regional_costs(
    path = 'examples/Operation_teaching/plots/regionalcosts_bytechs.html',
    stacked_by = 'techs'
)
