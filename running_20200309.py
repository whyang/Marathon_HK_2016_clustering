"""
Created on Mar. 5, 2020
@author: whyang
load dataset for running analytics
"""
# -*- coding: utf-8 -*-
import os
from ci_package.load_dataset import loadRunningData
from ci_package.cluster_dataset import clusterRunningData

###
# function of entry point
#
def doloadData():
    print('load running dataset')  
    # read running dataset
    loadrd = loadRunningData()
    loadrd.readCSV(datapath='.\\data') 

def doclusterData():
    print('cluster running dataset')  
    # cluster running dataset
    clusterrd = clusterRunningData()
    clusterrd.clustering(datapath='.\\data') #, clusters=50) # default 10 groups
  
###
# main program
#
if __name__ == '__main__':
    # set configuration info.
    figurepath = '.\\figure'  # directory of output folder 
    if not os.path.isdir(figurepath):
        os.mkdir(figurepath)

    datapath = '.\\data'  # directory of input data folder 
    if not os.path.isdir(datapath):
        os.mkdir(datapath)

    ##
    # conduct data cleasing and transforming raw data to CSV file for analysis
    #doloadData()
    
    ##
    # cluster runners' performance record as n groups
    doclusterData()
    
###############
# end of file #
###############