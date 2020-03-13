"""
Created on Mar. 12, 2020
@author: whyang

analyze the dataset of Marathon HK 2016
"""

###
# USAGE (example of command)
# python HKMarathon2016.py --switch e 
# python HKMarathon2016.py --switch c --cluster 10 
##

# -*- coding: utf-8 -*-
import os
import argparse
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

def doclusterData(numCluster=10):
    print('cluster running dataset')  
    # cluster running dataset
    clusterrd = clusterRunningData()
    clusterrd.clustering(clusters=numCluster, datapath='.\\data') #, clusters=50) # default 10 groups
  
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

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--switch', required=True, help='switch on e or c (etl or clustering)')
    ap.add_argument('-c', '--cluster', help='clustering the dataset of HK Marathon 2016')
    args = vars(ap.parse_args())
    
    if (args['switch'] == 'e')|(args['switch'] == 'etl'):
        # conduct data cleasing and transforming raw data to CSV file for analysis
        doloadData()
    elif (args['switch'] == 'c')|(args['switch'] == 'clustering'):
        # cluster runners' performanc        
        if (int(args['cluster']) <= 1):
            doclusterData()
        else:
            doclusterData(numCluster=int(args['cluster']))

###############
# end of file #
###############