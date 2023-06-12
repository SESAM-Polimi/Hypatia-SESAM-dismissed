"""
Italy MODEL - Hydrogen
Planning mode
"""

# Import of the Model

from hypatia import Model
import os
from hypatia import Plotter
from hypatia import Merge_results

#%% Sets 

# Create the model using as input the sets files

Ensure_Feasibility = "Yes"                                               # "Yes" alHighs unmet demand, "No" otherwise                                               

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


#%% GreenDeal
 
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

#%% GD+BAN Low Hydrogen Share

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

#%% GD+BAN Low Hydrogen Share - CT20

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

#%% GD+BAN Low Hydrogen Share - CT60

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

#%% GD+BAN Low Hydrogen Share - CT120

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

#%% GD+BAN Low Hydrogen Share - LR19 

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

#%% GD+BAN Low Hydrogen Share - LR19 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR19 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR19 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR22 

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

#%% GD+BAN Low Hydrogen Share - LR22 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR22 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR22 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR25

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

#%% GD+BAN Low Hydrogen Share - LR25 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR25 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR25 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR28

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

#%% GD+BAN Low Hydrogen Share - LR28 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR28 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR28 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR31

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

#%% GD+BAN Low Hydrogen Share - LR31 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR31 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR31 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR34

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

#%% GD+BAN Low Hydrogen Share - LR34 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR34 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR34 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR37

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

#%% GD+BAN Low Hydrogen Share - LR37 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR37 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR37 - CT120

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

#%% GD+BAN Low Hydrogen Share - LR40

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

#%% GD+BAN Low Hydrogen Share - LR40 - CT20

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

#%% GD+BAN Low Hydrogen Share - LR40 - CT60

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

#%% GD+BAN Low Hydrogen Share - LR40 - CT120

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

#%% GD+BAN High Hydrogen Share

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

#%% GD+BAN High Hydrogen Share - CT20

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

#%% GD+BAN High Hydrogen Share - CT60

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

#%% GD+BAN High Hydrogen Share - CT120

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

#%% GD+BAN High Hydrogen Share - LR19 

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

#%% GD+BAN High Hydrogen Share - LR19 - CT20

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

#%% GD+BAN High Hydrogen Share - LR19 - CT60

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

#%% GD+BAN High Hydrogen Share - LR19 - CT120

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

#%% GD+BAN High Hydrogen Share - LR22 

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

#%% GD+BAN High Hydrogen Share - LR22 - CT20

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

#%% GD+BAN High Hydrogen Share - LR22 - CT60

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

#%% GD+BAN High Hydrogen Share - LR22 - CT120

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

#%% GD+BAN High Hydrogen Share - LR25

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

#%% GD+BAN High Hydrogen Share - LR25 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v52")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v52"):
    os.mkdir("ENI/results_planning_v52")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v52",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR25 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v53")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v53"):
    os.mkdir("ENI/results_planning_v53")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v53",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR25 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v54")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v54"):
    os.mkdir("ENI/results_planning_v54")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v54",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR28

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v55")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v55"):
    os.mkdir("ENI/results_planning_v55")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v55",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR28 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v56")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v56"):
    os.mkdir("ENI/results_planning_v56")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v56",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR28 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v57")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v57"):
    os.mkdir("ENI/results_planning_v57")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v57",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR28 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v58")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v58"):
    os.mkdir("ENI/results_planning_v58")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v58",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR31

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v59")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v59"):
    os.mkdir("ENI/results_planning_v59")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v59",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR31 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v60")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v60"):
    os.mkdir("ENI/results_planning_v60")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v60",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR31 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v61")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v61"):
    os.mkdir("ENI/results_planning_v61")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v61",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR31 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v62")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v62"):
    os.mkdir("ENI/results_planning_v62")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v62",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR34

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v63")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v63"):
    os.mkdir("ENI/results_planning_v63")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v63",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR34 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v64")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v64"):
    os.mkdir("ENI/results_planning_v64")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v64",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR34 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v65")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v65"):
    os.mkdir("ENI/results_planning_v65")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v65",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR34 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v66")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v66"):
    os.mkdir("ENI/results_planning_v66")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v66",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR37

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v67")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v67"):
    os.mkdir("ENI/results_planning_v67")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v67",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR37 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v68")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v68"):
    os.mkdir("ENI/results_planning_v68")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v68",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR37 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v69")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v69"):
    os.mkdir("ENI/results_planning_v69")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v69",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR37 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v70")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v70"):
    os.mkdir("ENI/results_planning_v70")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v70",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR40

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v71")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v71"):
    os.mkdir("ENI/results_planning_v71")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v71",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR40 - CT20

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v72")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v72"):
    os.mkdir("ENI/results_planning_v72")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v72",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR40 - CT60

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v73")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v73"):
    os.mkdir("ENI/results_planning_v73")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v73",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% GD+BAN High Hydrogen Share - LR40 - CT120

# Read the parameters

Utopia.read_input_data("ENI/parameters_planning_v74")         # Path to the parameters folder
 
# Run the model to find the optimal solution

Utopia.run(
    solver='gurobi',                                                    # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)

# Create results and plots folder    
    
if not os.path.exists("ENI/results_planning_v74"):
    os.mkdir("ENI/results_planning_v74")

# Save the results as csv file in the previous folder

Utopia.to_csv(
    path= "ENI/results_planning_v74",                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%%
# Merge result csv for different scenarios
Merge_results(
    scenarios={
        "scenario1": "ENI" + "/results_planning_v1",
        "scenario2": "ENI" + "/results_planning_v2/",
        "scenario3": "ENI" + "/results_planning_v3/",
        "scenario4": "ENI" + "/results_planning_v4/",
        "scenario5": "ENI" + "/results_planning_v5/",
        "scenario6": "ENI" + "/results_planning_v6/",
        "scenario7": "ENI" + "/results_planning_v7/",
        "scenario8": "ENI" + "/results_planning_v8/",
        "scenario9": "ENI" + "/results_planning_v9/",
        "scenario10": "ENI" + "/results_planning_v10/",
        "scenario11": "ENI" + "/results_planning_v11/",
        "scenario12": "ENI" + "/results_planning_v12/",
        "scenario13": "ENI" + "/results_planning_v13/",
        "scenario14": "ENI" + "/results_planning_v14/",
        "scenario15": "ENI" + "/results_planning_v15/",
        "scenario16": "ENI" + "/results_planning_v16/",
        "scenario17": "ENI" + "/results_planning_v17/",
        "scenario18": "ENI" + "/results_planning_v18/",
        "scenario19": "ENI" + "/results_planning_v19/",
        "scenario20": "ENI" + "/results_planning_v20/",
        "scenario21": "ENI" + "/results_planning_v21/",
        "scenario22": "ENI" + "/results_planning_v22/",
        "scenario23": "ENI" + "/results_planning_v23/",
        "scenario24": "ENI" + "/results_planning_v24/",
        "scenario25": "ENI" + "/results_planning_v25/",
        "scenario26": "ENI" + "/results_planning_v26/",
        "scenario27": "ENI" + "/results_planning_v27/",
        "scenario28": "ENI" + "/results_planning_v28/",
        "scenario29": "ENI" + "/results_planning_v29/",
        "scenario30": "ENI" + "/results_planning_v30/",
        "scenario31": "ENI" + "/results_planning_v31/",
        "scenario32": "ENI" + "/results_planning_v32/",
        "scenario33": "ENI" + "/results_planning_v33/",
        "scenario34": "ENI" + "/results_planning_v34/",
        "scenario35": "ENI" + "/results_planning_v35/",
        "scenario36": "ENI" + "/results_planning_v36/",
        "scenario37": "ENI" + "/results_planning_v37/",
        "scenario38": "ENI" + "/results_planning_v38/",
        "scenario39": "ENI" + "/results_planning_v39/",
        "scenario40": "ENI" + "/results_planning_v40/",
        "scenario41": "ENI" + "/results_planning_v41/",
        "scenario42": "ENI" + "/results_planning_v42/",
        "scenario43": "ENI" + "/results_planning_v43/",
        "scenario44": "ENI" + "/results_planning_v44/",
        "scenario45": "ENI" + "/results_planning_v45/",
        "scenario46": "ENI" + "/results_planning_v46/",
        "scenario47": "ENI" + "/results_planning_v47/",
        "scenario48": "ENI" + "/results_planning_v48/",
        "scenario49": "ENI" + "/results_planning_v49/",
        "scenario50": "ENI" + "/results_planning_v50/",
        "scenario51": "ENI" + "/results_planning_v51/",
        "scenario52": "ENI" + "/results_planning_v52/",
        "scenario53": "ENI" + "/results_planning_v53/",
        "scenario54": "ENI" + "/results_planning_v54/",
        "scenario55": "ENI" + "/results_planning_v55/",
        "scenario56": "ENI" + "/results_planning_v56/",
        "scenario57": "ENI" + "/results_planning_v57/",
        "scenario58": "ENI" + "/results_planning_v58/",
        "scenario59": "ENI" + "/results_planning_v59/",
        "scenario60": "ENI" + "/results_planning_v60/",
        "scenario61": "ENI" + "/results_planning_v61/",
        "scenario62": "ENI" + "/results_planning_v62/",
        "scenario63": "ENI" + "/results_planning_v63/",
        "scenario64": "ENI" + "/results_planning_v64/",
        "scenario65": "ENI" + "/results_planning_v65/",
        "scenario66": "ENI" + "/results_planning_v66/",
        "scenario67": "ENI" + "/results_planning_v67/",
        "scenario68": "ENI" + "/results_planning_v68/",
        "scenario69": "ENI" + "/results_planning_v69/",
        "scenario70": "ENI" + "/results_planning_v70/",
        "scenario71": "ENI" + "/results_planning_v71/",
        "scenario72": "ENI" + "/results_planning_v72/",
        "scenario73": "ENI" + "/results_planning_v73/",
        "scenario74": "ENI" + "/results_planning_v74/"
    },
    path="ENI" + "/merged_results_planning",
    force_rewrite=True
)