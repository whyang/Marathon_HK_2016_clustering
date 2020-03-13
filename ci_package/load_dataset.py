"""
Created on Mar. 5, 2020
@author: whyang

load the marathon running dataset of Hong Kong 2016 (一般馬拉松路跑) 
"""
# -*- coding: utf-8 -*-
import pandas as pd
import time 

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

#######################################################################################
# declare the function of load running data (Hong Kong 2016, 一般馬拉松路跑)
#######################################################################################
class loadRunningData:
    def __init__(self):
        pass       
    ###
    # read the running dataset
    #
    def readCSV(self, datapath='.\\data'):
        with open(datapath+'\\'+'marathon_HK2016_raw.csv', 'r', encoding='utf-8', newline='') as csvfile:
            df = pd.read_csv(
                    csvfile,
                    header = 0,
                    usecols = ['Overall_Position', 'Gender_Position', 'Category_Position', 'Category', 'Race_No',
                           'Country ', 'Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time'],
                    parse_dates=['Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time'],
                    verbose = True,
                    skip_blank_lines = True)
            df = trim_all_cells(df) # trim whitespace from each cell in dataframe            
            
            # 資料清洗
            # 當每筆資料欄內容有問題時(miss data)，剔除該筆資料
            df.dropna('index', inplace=True)            
                
            # 轉換跑步成績格式(hh:mm:ss)為秒(seconds)
            df['Official_Time'] = df['Official_Time'].apply(lambda x:time.mktime(x.timetuple()))
            df['Official_Time'] = df['Official_Time'].apply(lambda x:time.strftime('%H:%M:%S',time.localtime(x)))
            df['Official_Time'] = pd.to_timedelta(df['Official_Time']).astype('timedelta64[s]').astype(int)
            #
            df['Net_Time'] = df['Net_Time'].apply(lambda x:time.mktime(x.timetuple()))
            df['Net_Time'] = df['Net_Time'].apply(lambda x:time.strftime('%H:%M:%S',time.localtime(x)))
            df['Net_Time'] = pd.to_timedelta(df['Net_Time']).astype('timedelta64[s]').astype(int)
            #        
            df['tenkm_Time'] = df['tenkm_Time'].apply(lambda x:time.mktime(x.timetuple()))
            df['tenkm_Time'] = df['tenkm_Time'].apply(lambda x:time.strftime('%H:%M:%S',time.localtime(x)))
            df['tenkm_Time'] = pd.to_timedelta(df['tenkm_Time']).astype('timedelta64[s]').astype(int)
            #            
            df['Half_Way_Time'] = df['Half_Way_Time'].apply(lambda x:time.mktime(x.timetuple()))
            df['Half_Way_Time'] = df['Half_Way_Time'].apply(lambda x:time.strftime('%H:%M:%S',time.localtime(x)))
            df['Half_Way_Time'] = pd.to_timedelta(df['Half_Way_Time']).astype('timedelta64[s]').astype(int)
            #            
            df['thirtykm_Time'] = df['thirtykm_Time'].apply(lambda x:time.mktime(x.timetuple()))
            df['thirtykm_Time'] = df['thirtykm_Time'].apply(lambda x:time.strftime('%H:%M:%S',time.localtime(x)))
            df['thirtykm_Time'] = pd.to_timedelta(df['thirtykm_Time']).astype('timedelta64[s]').astype(int)           
        
            print('-----------')
            print(df)
            
            # 整理最後乾淨的資料集，存檔為CSV格式
            #        
            df.to_csv(datapath+'\\'+'marathon_HK2016.csv', 
                      index=False, 
                      encoding='cp950', 
                      sep=',') # for windows environment (encoding as ANSI format)
            
            print('Finish this work')
#
# end of loadRunningData
###

###############
# end of file #                                                                         
###############
