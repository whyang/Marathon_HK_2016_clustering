"""
Created on Mar. 5, 2020
@author: whyang

cluster the marathon running dataset of Hong Kong 2016 (一般馬拉松路跑) 
"""
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #繪製3D座標的函式

#######################################################################################
# declare functions
#######################################################################################
###
# remove leading and trailing characters of each value across all cells in dataframe
#
def trim_all_cells(df):
    # trim whitespace from ends of each value across all series in dataframe
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

def normalize(x, axis, method, minmax_range =(0,1)):
    if method == 'z-score':
        scale_a = preprocessing.scale(x, axis=axis)
    elif method== 'minmax':    
        scale_a = preprocessing.minmax_scale(x, axis=axis, feature_range=minmax_range) #default feature range 0~1
    return scale_a

#######################################################################################
# declare the function of load running data (Hong Kong 2016, 一般馬拉松路跑)
#######################################################################################
class clusterRunningData:
    def __init__(self):
        pass       
    ###
    # cluster the running dataset
    #        
    def clustering(self, clusters=10, datapath='.\\data', figurepath='.\\figure'):
        with open(datapath+'\\'+'marathon_HK2016.csv', 'r', encoding='utf-8', newline='') as csvfile:
            df = pd.read_csv(
                    csvfile,
                    header = 0,
                    usecols = ['Overall_Position', #'Gender_Position', 'Category_Position', 'Category', 'Race_No', 'Country ', 
                               'Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time'],
                    parse_dates=['Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time'],
                    verbose = True,
                    skip_blank_lines = True)

            # normalize the each metrices of the running performance
            axis = 0
            df['Official_Time'] = normalize(df['Official_Time'], axis, method='minmax', minmax_range=(0, 1))
            df['Net_Time'] = normalize(df['Net_Time'], axis, method='minmax', minmax_range=(0, 1))
            df['tenkm_Time'] = normalize(df['tenkm_Time'], axis, method='minmax', minmax_range=(0, 1))
            df['Half_Way_Time'] = normalize(df['Half_Way_Time'], axis, method='minmax', minmax_range=(0, 1))
            df['thirtykm_Time'] = normalize(df['thirtykm_Time'], axis, method='minmax', minmax_range=(0, 1))

            # conduct clustering (adopt KMeans algorithm)
            #clusters = 10 # given n groups if n is not 10
            kmeans = KMeans(n_clusters = clusters)
            y_pred = kmeans.fit_predict(df)
            
            # I'm confused about the assigned object's data type/structure (label), in terms of the y_pred
            # y_pred.T and not use transpose, both of them are the same
            print(y_pred.transpose())
            print('----------------')
            print(y_pred)
            
            # amend the clustering labels w.r.t each running record
            df['label']=y_pred.T
            print(df)
    
            # generate the output file which are clustered adopting sklearn.cluster.KMeans
            df.to_csv(datapath+'\\'+'marathon_HK2016_clustering.csv',
                      index=False, 
                      encoding='cp950', 
                      sep=',') # for windows environment (encoding as ANSI format)
            
            # present the clustering result
            plt.figure(figsize=(12, 12))
            #plt.subplot(221)
            plt.scatter(df['Official_Time'], df['Half_Way_Time'], c=y_pred)
            plt.title('Marathon HK 2016')
            #ax1.set_title("The silhouette plot for the various clusters.")
            plt.xlabel('Official_Time')
            plt.ylabel("Half_Way_Time")

            # print out figure to a file 
            figName = figurepath + '\\' + 'marathon_HK2016_cluster10(2D).png'
            plt.savefig(figName) # print out the selected firgure format (PNG)
            plt.show()#顯示模組中的所有繪圖物件
             
            fig=plt.figure(figsize=(12, 12)) #建立一個繪圖物件
            ax = Axes3D(fig) #, rect=[0, 0, .95, 1], elev=48, azim=134) #用這個繪圖物件建立一個Axes物件(有3D座標)
            ax.scatter(df['Official_Time'], df['Half_Way_Time'], df['tenkm_Time'], c=y_pred.astype(np.float), edgecolor='k')
            #ax.w_xaxis.set_ticklabels([])
            #ax.w_yaxis.set_ticklabels([])
            #ax.w_zaxis.set_ticklabels([])
            ax.set_xlabel('Official_Time')
            ax.set_ylabel('Half_Way_Time')
            ax.set_zlabel('10km_Time')
            ax.set_title('Marathon HK 2016')
            #ax.dist = 12
            figName = figurepath + '\\' + 'marathon_HK2016_cluster10(3D).png'
            fig.savefig(figName) # print out the selected firgure format (PNG)
            fig.show() #顯示模組中的所有繪圖物件
            
            print('Finish this work')        
#
# end of clusterRunningData
###

###############
# end of file #                                                                         
###############
