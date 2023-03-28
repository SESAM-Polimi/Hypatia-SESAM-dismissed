# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:14:52 2022

@author: Gianluca Pellecchia

Using k-means method for the clustering of hourly load profile

"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

hourly_demand = pd.read_excel("Clustering input data.xlsx", sheet_name="Foglio1") 
x = np.arange(1,25)

df = np.reshape(hourly_demand.values, (365, 24))
df = np.transpose(df)
df = pd.DataFrame(df)

# for i in range(0,365):
#     df.rename(columns={i:"day"+str(i)}, inplace = True)

# for col in df1.columns:
#     plt.plot(x,df1[col])

scaler = MinMaxScaler()
scaler.fit(hourly_demand)
df1 = scaler.transform(hourly_demand)
df1 = pd.DataFrame(np.transpose(np.reshape(df1, (365,24))))
for i in range(0,365):
    df1.rename(columns={i:"day"+str(i)}, inplace = True)

for col in df1.columns:
    plt.figure(0)
    plt.plot(x,df1[col])

df_final = df1.T
# norm=df1.to_dict('series')
km = KMeans(n_clusters=3)
y_predict = km.fit_predict(df_final)

df_final.insert(0,"cluster",y_predict)
# df_final['cluster'] = y_predict
df_final.head()

c1 = df_final[df_final.cluster==0]
c2 = df_final[df_final.cluster==1]
c3 = df_final[df_final.cluster==2]

cluster1 = c1.drop(c1.columns[0],axis=1).T
cluster2 = c2.drop(c2.columns[0],axis=1).T
cluster3 = c3.drop(c3.columns[0],axis=1).T
    
for col in cluster1.columns:
    plt.figure(1)
    plt.plot(x,cluster1[col])
    
center_clust1 = km.cluster_centers_[:,0]
plt.plot(km.cluster_centers_[:,0], color='black')
    
for col in cluster2.columns:
    plt.figure(2)
    clust2 = plt.plot(x,cluster2[col])
    
for col in cluster3.columns:
    plt.figure(3)
    clust3 = plt.plot(x,cluster3[col])