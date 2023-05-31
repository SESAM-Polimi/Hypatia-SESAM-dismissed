"""
Utopia MODEL
Planning mode
"""

# Import of the Model

from hypatia import Model
import os
from hypatia import Plotter

#%% Sets Without Biorefineries

# Create the model using as input the sets files

Ensure_Feasibility = "Yes"                                               # "Yes" allows unmet demand, "No" otherwise                                               

Utopia = Model(
    path="ENI/sets_planning_v1",                             # Path to the sets folder
    mode="Planning",                                                    # "Planning" or "Operation" mode
    ensure_feasibility = Ensure_Feasibility                                     
)

# Create the parameters with default values

# Utopia.create_data_excels(
#     path ='ENI/parameters_planning_v1',                      # Path to the parameters folder
#     force_rewrite=True                                                  # Overwrite the parameters files (True) or not (False)
# )

#%% Basecase

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v1")         # Path to the parameters folder

# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v1"):
    os.mkdir("ENI/results_planning_v1")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v1",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)


#%% GD without biorefineries
 
# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v2")         # Path to the parameters folder

# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v2"):
    os.mkdir("ENI/results_planning_v2")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v2",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN without biorefineries

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v3")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v3"):
    os.mkdir("ENI/results_planning_v3")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v3",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% Sets With Biorefiners

# Create the model using as input the sets files

Ensure_Feasibility = "Yes"                                               # "Yes" allows unmet demand, "No" otherwise                                               

Utopia = Model(
    path="ENI/sets_planning_v2",                             # Path to the sets folder
    mode="Planning",                                                    # "Planning" or "Operation" mode
    ensure_feasibility = Ensure_Feasibility                                     
)

# Create the parameters with default values

# Utopia.create_data_excels(
#     path ='ENI/parameters_planning_v4',                      # Path to the parameters folder
#     force_rewrite=True                                                  # Overwrite the parameters files (True) or not (False)
# )

#%% GD+BAN Low Biofuels Share

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v4")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v4"):
    os.mkdir("ENI/results_planning_v4")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v4",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN Average Biofuels Share

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v5")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v5"):
    os.mkdir("ENI/results_planning_v5")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v5",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Biofuels Share

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v6")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v6"):
    os.mkdir("ENI/results_planning_v6")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v6",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 120NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v7")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v7"):
    os.mkdir("ENI/results_planning_v7")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v7",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 120NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v8")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v8"):
    os.mkdir("ENI/results_planning_v8")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v8",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% HIGH SHARE + 120NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v9")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v9"):
    os.mkdir("ENI/results_planning_v9")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v9",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 100NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v10")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v10"):
    os.mkdir("ENI/results_planning_v10")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v10",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 80NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v11")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v11"):
    os.mkdir("ENI/results_planning_v11")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v11",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 60NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v12")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v12"):
    os.mkdir("ENI/results_planning_v12")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v12",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 40NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v13")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v13"):
    os.mkdir("ENI/results_planning_v13")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v13",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 20NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v14")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v14"):
    os.mkdir("ENI/results_planning_v14")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v14",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 120NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v15")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v15"):
    os.mkdir("ENI/results_planning_v15")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v15",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 120NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v16")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v16"):
    os.mkdir("ENI/results_planning_v16")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v16",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 120NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v17")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v17"):
    os.mkdir("ENI/results_planning_v17")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v17",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 120NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v18")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v18"):
    os.mkdir("ENI/results_planning_v18")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v18",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 100NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v19")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v19"):
    os.mkdir("ENI/results_planning_v19")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v19",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 100NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v20")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v20"):
    os.mkdir("ENI/results_planning_v20")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v20",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 100NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v21")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v21"):
    os.mkdir("ENI/results_planning_v21")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v21",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 100NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v22")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v22"):
    os.mkdir("ENI/results_planning_v22")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v22",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 40NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v23")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v23"):
    os.mkdir("ENI/results_planning_v23")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v23",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 40NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v24")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v24"):
    os.mkdir("ENI/results_planning_v24")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v24",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 40NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v25")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v25"):
    os.mkdir("ENI/results_planning_v25")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v25",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 40NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v26")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v26"):
    os.mkdir("ENI/results_planning_v26")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v26",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 20NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v27")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v27"):
    os.mkdir("ENI/results_planning_v27")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v27",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 20NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v28")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v28"):
    os.mkdir("ENI/results_planning_v28")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v28",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 20NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v29")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v29"):
    os.mkdir("ENI/results_planning_v29")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v29",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% AV SHARE + 20NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v30")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v30"):
    os.mkdir("ENI/results_planning_v30")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v30",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 100NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v31")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v31"):
    os.mkdir("ENI/results_planning_v31")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v31",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 80NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v32")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v32"):
    os.mkdir("ENI/results_planning_v32")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v32",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 60NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v33")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v33"):
    os.mkdir("ENI/results_planning_v33")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v33",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 40NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v34")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v34"):
    os.mkdir("ENI/results_planning_v34")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v34",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 20NG

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v35")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v35"):
    os.mkdir("ENI/results_planning_v35")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v35",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 120NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v36")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v36"):
    os.mkdir("ENI/results_planning_v36")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v36",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 120NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v37")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v37"):
    os.mkdir("ENI/results_planning_v37")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v37",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 120NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v38")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v38"):
    os.mkdir("ENI/results_planning_v38")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v38",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 120NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v39")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v39"):
    os.mkdir("ENI/results_planning_v39")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v39",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 100NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v40")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v40"):
    os.mkdir("ENI/results_planning_v40")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v40",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 100NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v41")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v41"):
    os.mkdir("ENI/results_planning_v41")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v41",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 100NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v42")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v42"):
    os.mkdir("ENI/results_planning_v42")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v42",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 100NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v43")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v43"):
    os.mkdir("ENI/results_planning_v43")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v43",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 40NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v44")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v44"):
    os.mkdir("ENI/results_planning_v44")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v44",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 40NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v45")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v45"):
    os.mkdir("ENI/results_planning_v45")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v45",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 40NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v46")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v46"):
    os.mkdir("ENI/results_planning_v46")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v46",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 40NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v47")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v47"):
    os.mkdir("ENI/results_planning_v47")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v47",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 20NG + 20CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v48")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v48"):
    os.mkdir("ENI/results_planning_v48")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v48",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 20NG + 40CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v49")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v49"):
    os.mkdir("ENI/results_planning_v49")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v49",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 20NG + 80CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v50")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v50"):
    os.mkdir("ENI/results_planning_v50")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v50",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% LOW SHARE + 20NG + 120CT

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v51")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v51"):
    os.mkdir("ENI/results_planning_v51")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v51",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)