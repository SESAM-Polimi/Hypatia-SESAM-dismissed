# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:55:02 2022

@author: Gianluca Pellecchia
"""

import pandas as pd
import numpy as np

#%%

yearly_demand = pd.read_excel("Input_demand.xlsx", sheet_name="Sheet1") 
time_series = pd.read_excel("Time_series_demand.xlsx", sheet_name="Sheet1")

num_rows, num_cols = yearly_demand.shape
num_years = num_rows

demand = []
for i in range(0,num_rows):
    a = [yearly_demand.iloc[i]]
    demand_hourly = np.repeat([yearly_demand.iloc[i]], 8760, axis=0)
    demand.append(np.multiply(demand_hourly,time_series))
demand_total = np.vstack(demand)

# demand_hourly = np.zeros((8760,num_cols))
# demand = []
# for i in range(0,num_rows):
#     for j in range(0,8760):
#         demand_hourly[j,:] = yearly_demand.iloc[i]
#     demand.append(np.multiply(demand_hourly,time_series))
# demand_total = np.vstack(demand)

#%%
num_rows, num_cols = demand_total.shape

# avg = np.zeros((24*num_years,6))
average_dem= []
for h in range(0,num_rows,8760):
    demand_year = demand_total[h:(h+8760),:]
    for r in range(0,24,1):
        d = np.zeros((1,num_cols))
        for i in range(r,8760,24):
            d += demand_year[i,:]
        avg = d/365
        average_dem.append(avg)
average_demand = np.vstack(average_dem)
        
        
df = pd.DataFrame(average_demand)
df1 = df.set_axis(['Export', 'Primary', 'Transport', 'Industry', 'Residential', 'Services'], axis=1, inplace=False)
df1.to_excel('Average_demand.xlsx')

#%%

carrier_in = pd.read_excel("Input_carrier.xlsx", sheet_name="Sheet1")
n_rows, n_cols = carrier_in.shape

carrier_ratio = np.repeat(carrier_in.values, 24, axis=0)

dff = pd.DataFrame(carrier_ratio)
dff.to_excel('Carrier_ratio_in.xlsx')




