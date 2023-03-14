"""
Utopia MODEL
Operation mode
"""

from hypatia import Model
import os
from hypatia import Merge_results
from hypatia import Plotter

#%% 
Utopia = Model(path="examples/Operation/sets_operation", mode="Operation")

#%% 
Utopia.create_data_excels(
    path ='examples\parameters_operation',
    force_rewrite=True
)

#%% 
Utopia.read_input_data("examples\Operation\parameters_operation")

#%% 
Utopia.run(solver='gurobi',verbosity=True, force_rewrite= True)

#%% 
os.mkdir("examples/Operation/results_operation/")

#%% 
Utopia.to_csv(path='examples/Operation/results_operation', force_rewrite=True, postprocessing_module="aggregated")

#%% 
Utopia.create_config_file(
  path = 'examples/Operation/config_operation.xlsx'
)

#%% 
plots = Plotter(
  results = Utopia,
  config = 'examples/Operation/config_operation.xlsx',
  hourly_resolution = True, # if model has an hourly resultion otherwise False
)

#%% 
plots.plot_total_capacity(
    path = 'examples/Operation/plots_operation/totalcapacity.html',
    tech_group = 'Power Generation',
    kind="bar",
    decom_cap=True,
)

#%% 
plots.plot_prod_by_tech(
    path = 'examples/Operation/plots_operation/prod_by_tech.html',
    tech_group = 'Power Generation',
    kind="bar",
)

#%% 
plots.plot_use_by_technology(
    path = 'examples/Operation/plots_operation/use_by_tech.html',
    fuel_group = 'Oil',
    kind="bar",
)

#%%
plots.plot_fuel_prod_cons(
    path = 'examples/Operation/plots_operation/prod_con_share.html',
    years = ["Y0"],
    fuel_group = 'Electricity',
    trade=False,
)
#%% 
plots.plot_emissions(
    path = 'examples/Operation/plots_operation/emissions.html',
    tech_group = 'Power Generation',
    emission_type = ["CO2 emissions"],
    kind="bar",
    aggregate=False
)

#%%
plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation/plots_operation/hourlyprod.html',
    tech_group = 'Power Generation',
    fuel_group = 'Electricity',
    kind = "bar",
    year = ["Y0"],
    start="01-01-2019 00:00:00",
    end="01-01-2019 23:00:00",
)

#%%
plots.plot_regional_costs(
    path = 'examples/Operation/plots_operation/regionalcosts_bytechs.html',
    stacked_by = 'techs'
)
