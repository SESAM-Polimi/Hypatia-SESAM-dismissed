# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:25:55 2022

@author: Gianluca Pellecchia
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from tslearn.clustering import TimeSeriesKMeans, silhouette_score
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from kneed import KneeLocator

yearly_demand = pd.read_excel("Input_demand.xlsx", sheet_name="Sheet1") 
time_series = pd.read_excel("Time_series_demand.xlsx", sheet_name="Sheet1")

num_rows, num_cols = yearly_demand.shape
num_years = num_rows

demand = []
for i in range(0,num_rows):
    demand_hourly = np.repeat([yearly_demand.iloc[i]], 8760, axis=0)
    demand.append(np.multiply(demand_hourly,time_series))
    
sector_demand = np.reshape(demand[0].iloc[:,0].values, (365,24))

for col in range(1,demand[0].shape[1]):
    sector_demand_other = np.reshape(demand[0].iloc[:,col].values, (365,24))
    sector_demand = np.hstack((sector_demand,sector_demand_other))
    
df = pd.DataFrame(sector_demand)

for i in range(0,365):
    df.rename(index={i:"day"+str(i)}, inplace = True)

#%% evaluating optimal number of cluster with dtw method and elbow method
k_rng = range(1,11)
SSE = []
for k in k_rng:   
    # starting clustering
    norm_hourly_demand = TimeSeriesScalerMeanVariance().fit_transform(df)
    model = TimeSeriesKMeans(n_clusters=k, metric="dtw", dtw_inertia=True)
    model.fit(norm_hourly_demand) 
    y_pred = model.fit_predict(norm_hourly_demand)
    SSE.append(model.inertia_)
    
plt.figure()
plt.plot(k_rng,SSE)
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")

kl = KneeLocator(k_rng, SSE, curve="convex", direction="decreasing")
k = kl.elbow

#%% starting clustering
norm_hourly_demand = TimeSeriesScalerMeanVariance().fit_transform(df)
model1 = TimeSeriesKMeans(n_clusters=k, metric="dtw", max_iter=10)
model1.fit(norm_hourly_demand)
y_pred = model1.fit_predict(norm_hourly_demand)

cluster_centers1 = pd.DataFrame()
plt.figure()
for yi in range(k):
    plt.subplot(3, 3, 4 + yi)
    cluster_centers1['Cluster'+str(yi)] = model1.cluster_centers_[yi].ravel()
    for xx in model1._X_fit[y_pred == yi]:
        plt.plot(xx.ravel(), "k-", alpha=.2)
    plt.plot(model1.cluster_centers_[yi].ravel(), "r-")       

df.insert(0,"Cluster",y_pred)
df.head()
 
clusters = {}
for i in range(k):
    clusters['Cluster '+str(i+1)] = df[df.Cluster==i].loc[:,df.columns != 'Cluster']

#%%
sectors = {}        
for g in range(0,df.shape[1]-1, 24):
        cluster_sectors = {}
        for i in range(k):
            cluster_sectors['Cluster '+str(i+1)] = df[df.Cluster==i].loc[:,df.columns != 'Cluster'].loc[:, g:g+23]
        sectors[g] = cluster_sectors
      
sectors['Sector 1'] = sectors.pop(0)
sectors['Sector 2'] = sectors.pop(24)
sectors['Sector 3'] = sectors.pop(48)
sectors['Sector 4'] = sectors.pop(72)
sectors['Sector 5'] = sectors.pop(96)
sectors['Sector 6'] = sectors.pop(120)

#%%
x=range(1,25)
hh = pd.DataFrame()
sectors_means = {}
for key in sectors.keys():
    cluster_mean = {}
    for xx, yy in sectors[key].items():  
        plt.figure()
        plt.plot(x,yy.T, "k-", alpha=.2)
        plt.plot(x,yy.T.mean(axis=1), "r-")
        plt.xlabel('Hours')
        plt.ylabel('Load demand')
        plt.title(str(key)+ '-' + str(xx))
        cluster_mean['Mean '+str(xx)] = yy.T.mean(axis=1)
        hh = pd.DataFrame.from_dict(cluster_mean) 
    sectors_means[key] = cluster_mean
    
#%% 
for key in sectors_means.keys():
    reduced_demand = pd.DataFrame()
    for xx, yy in sectors_means[key].items():
        reduced_demand = pd.concat([reduced_demand,yy],axis=1)
    reduced_demand = pd.DataFrame(np.reshape(reduced_demand.T.values, (24*k, 1)))
    plt.figure()
    plt.plot(range(1,24*k+1),reduced_demand)
    plt.xlabel('Hours')
    plt.ylabel('Demand')
    plt.title(str(key)+': Reduced yearly demand')

#%%
# #%% evaluating optimal number of cluster with dtw method and silhoutte coefficients method
# k_rng = range(2,11)
# silhouette_coefficients  = []
# for k in k_rng:   
#     norm_hourly_demand = TimeSeriesScalerMeanVariance().fit_transform(df)
#     model = TimeSeriesKMeans(n_clusters=k, metric="dtw", dtw_inertia=True)
#     model.fit(norm_hourly_demand) 
#     y_pred = model.fit_predict(norm_hourly_demand)
#     score = silhouette_score(norm_hourly_demand, model.labels_,metric="dtw")
#     silhouette_coefficients.append(score)
    
# plt.figure()
# plt.plot(k_rng,silhouette_coefficients)
# plt.xlabel("Number of Clusters")
# plt.ylabel("silhouette coefficients")

# max_silhouette_coefficients=max(silhouette_coefficients)
# k1 = silhouette_coefficients.index(max_silhouette_coefficients)+2

# #%% evaluating optimal number of cluster with euclidean method
# SSE1 = []
# for k in k_rng:   
#     # starting clustering
#     norm_hourly_demand = TimeSeriesScalerMeanVariance().fit_transform(df)
#     model1 = TimeSeriesKMeans(n_clusters=k, metric="euclidean", dtw_inertia=True)
#     model1.fit(norm_hourly_demand) 
#     y_pred1 = model1.fit_predict(norm_hourly_demand)
#     SSE1.append(model1.inertia_)
    
# plt.figure()
# plt.plot(k_rng,SSE1)
   



