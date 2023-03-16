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

Utopia = Model(path="examples/Operation_teaching/sets", mode="Planning")

Utopia.create_data_excels(
    path ='examples\Operation_teaching\parameters',                      
    force_rewrite=True                                                  
)

Utopia.read_input_data("examples\Operation_teaching\parameters")

Utopia.run(solver='gurobi',verbosity=True, force_rewrite= True)

os.mkdir("examples/Operation_teaching/results/")  

Utopia.to_csv(path='examples/Operation_teaching/results', force_rewrite=True, postprocessing_module="aggregated")

plots = Plotter(
  results = Utopia,
  config = 'examples/Operation_teaching/config.xlsx',
  hourly_resolution = True, # if model has an hourly resultion otherwise False
)

plots.plot_total_capacity(
    path = 'examples/Operation_teaching/plots/totalcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
    decom_cap=True,
)

plots.plot_prod_by_tech(
    path = 'examples/Operation_teaching/plots/prod_by_tech.html',
    tech_group = 'Power Generation',
    kind="bar",
)

plots.plot_use_by_technology(
    path = 'examples/Operation_teaching/plots/use_by_tech.html',
    fuel_group = 'Oil',
    kind="bar",
)

plots.plot_fuel_prod_cons(
    path = 'examples/Operation_teaching/plots/prod_con_share__.html',
    years = ["Y0"],
    fuel_group = 'Electricity',
    trade=False,
)

plots.plot_emissions(
    path = 'examples/Operation_teaching/plots/emissions.html',
    tech_group = 'Power Generation',
    emission_type = ["CO2"],
    kind="bar",
    aggregate=True
)

plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation_teaching/plots/hourlyprod.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y0"],
    start="01-01-2020 00:00:00",
    end="01-01-2020 23:00:00",
)

plots.plot_regional_costs(
    path = 'examples/Operation_teaching/plots/regionalcosts_bytechs.html',
    stacked_by = 'techs'
)
