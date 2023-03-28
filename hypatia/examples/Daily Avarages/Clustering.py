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

hourly_demand = pd.read_excel("Clustering input data.xlsx", sheet_name="Foglio1") 
x = np.arange(1,25)

df = np.reshape(hourly_demand.values, (365, 24))
df = pd.DataFrame(df)

for i in range(0,365):
    df.rename(index={i:"day"+str(i)}, inplace = True)
    
'''    
evaluating optimal number of cluster with dtw method and elbow method
'''

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

x=range(1,25)
cluster_mean = pd.DataFrame()
for xx, yy in clusters.items():  
    plt.figure()
    plt.plot(x,yy.T, "k-", alpha=.2)
    plt.plot(x,yy.T.mean(axis=1), "r-")
    plt.xlabel('Hours')
    plt.ylabel('Load demand')
    plt.title(str(xx))
    cluster_mean['mean_'+str(xx)] = yy.T.mean(axis=1)

#%% 
demand = pd.DataFrame(np.reshape(cluster_mean.T.values, (96, 1)))
yearly_demand = pd.DataFrame()
yearly_demand['Year 1'] = demand
plt.figure()
plt.plot(yearly_demand)
plt.xlabel('Hours')
plt.ylabel('Demand')
plt.title('Reduced yearly demand')





