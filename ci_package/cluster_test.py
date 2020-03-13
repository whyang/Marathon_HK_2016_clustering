# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:35:53 2020

@author: whyang
"""
import pandas as pd
import time

def trim_all_cells(df):
    # trim whitespace from ends of each value across all series in dataframe
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)

datapath = '..\\data'
with open(datapath+'\\'+'marathon_HK2016_raw.csv', 'r', encoding='utf-8', newline='') as csvfile:
    df = pd.read_csv(
            csvfile,
            header = 0,
            usecols = ['Overall_Position', 'Gender_Position', 'Category_Position', 'Category', 'Race_No',
                       'Country ', 'Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time'],
            verbose = True,
            skip_blank_lines = True,
            parse_dates=['Official_Time', 'Net_Time', 'tenkm_Time', 'Half_Way_Time', 'thirtykm_Time']) 
            #date_parser=dateparse) 
    
    df = trim_all_cells(df) # trim whitespace from each cell in dataframe
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
        
    df.to_csv(datapath+'\\'+'marathon_HK2016_20200312.csv', 
              index=False, 
              encoding='cp950', 
              sep=',') # for windows environment (encoding as ANSI format)
    print(df)
    print(df.dtypes)

    '''               
   # df = trim_all_cells(df) # trim whitespace from each cell in dataframe
         
            # 轉換成績欄的數據資料格式為'datatime'
            # 指定當raw data有錯誤發生時(沒有值或是其它格式轉為datetime有錯時)，直接取代為'NaT'
            df['Official_Time'] = pd.to_datetime(df['Official_Time'], errors='coerce')
            df['Net_Time'] = pd.to_datetime(df['Net_Time'], errors='coerce')
            df['tenkm_Time'] = pd.to_datetime(df['tenkm_Time'], errors='coerce')
            df['Half_Way_Time'] = pd.to_datetime(df['Half_Way_Time'], errors='coerce')
            df['thirtykm_Time'] = pd.to_datetime(df['thirtykm_Time'], errors='coerce')
            
            # 資料清洗
            # 當跑步成績(上述5個)欄有問題時，剔除該筆資料
            df.loc[(df.Official_Time == np.datetime64('NaT')), 'selected'] = np.nan # mark for discarding
            df.loc[(df.Net_Time == np.datetime64('NaT')), 'selected'] = np.nan # mark for discarding
            df.loc[(np.isnat(df.tenkm_Time)), 'selected'] = np.nan # mark for discarding
            df.loc[(np.isnat(df.Half_Way_Time)), 'selected'] = np.nan # mark for discarding
            df.loc[np.isnat(df.thirtykm_Time), 'selected'] = np.nan # mark all of the rows as null
            df.dropna(subset=['selected'], inplace=True) # conduct dropping of the row that are marked as NaN

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
            df.drop(columns=['selected'], inplace=True) # skip fields that are not used
            df.to_csv(datapath+'\\'+'marathon_HK2016.csv', 
                      index=False, 
                      encoding='cp950', 
                      sep=',') # for windows environment (encoding as ANSI format)
            
            print('Finish this work')
    '''