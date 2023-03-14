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

Utopia = Model(path="examples/Planning/sets_planning", mode="Planning")

Utopia.read_input_data("examples\Planning\parameters_planning")

Utopia.run(solver='gurobi',verbosity=True, force_rewrite= True)

Utopia.to_csv(path='examples/Planning/results_planning', force_rewrite=True, postprocessing_module="aggregated")

plots = Plotter(
  results = Utopia,
  config = 'examples/Planning/config_planning.xlsx',
  hourly_resolution = True, # if model has an hourly resultion otherwise False
)

plots.plot_total_capacity(
    path = 'examples/Planning/plots_planning/totalcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
    decom_cap=True,
)

plots.plot_new_capacity(
    path = 'examples/Planning/plots_planning/newcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
)

plots.plot_prod_by_tech(
    path = 'examples/Planning/plots_planning/prod_by_tech.html',
    tech_group = 'Power Generation',
    kind="bar",
)

plots.plot_use_by_technology(
    path = 'examples/Planning/plots_planning/use_by_tech.html',
    fuel_group = 'Oil',
    kind="bar",
)

plots.plot_fuel_prod_cons(
    path = 'examples/Planning/plots_planning/prod_con_share__.html',
    years = ["Y1"],
    fuel_group = 'Electricity',
    trade=False,
)

plots.plot_emissions(
    path = 'examples/Planning/plots_planning/emissions.html',
    tech_group = 'Power Generation',
    emission_type = ["CO2"],
    kind="bar",
    aggregate=True
)

plots.plot_hourly_prod_by_tech(
    path = 'examples/Planning/plots_planning/hourlyprod.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y3"],
    start="01-01-2022 00:00:00",
    end="01-01-2022 23:00:00",
)

plots.plot_regional_costs(
    path = 'examples/Planning/plots_planning/regionalcosts_bytechs.html',
    stacked_by = 'techs'
)
