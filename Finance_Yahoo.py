
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time
import datetime
from pprint import pprint
import json
import matplotlib

def stock_tables():

    def last_day_of_month_in_timestamp(month):
        next_month = datetime.date(2020, month, 1).replace(day=28) + datetime.timedelta(days=4)
        date = (next_month - datetime.timedelta(days=next_month.day))
        element = datetime.datetime.strptime(str(date),"%Y-%m-%d")
        return int(datetime.datetime.timestamp(element))

    def first_day_of_the_month_in_timestamp(month):
        date = datetime.datetime(2020, month, 1)
        element = datetime.datetime.strptime(str(date),"%Y-%m-%d %H:%M:%S")
        return int(datetime.datetime.timestamp(element))
        

    def stock_dataframes(stock):
        table_list = []
        for month in range(1, 9):
            start_date = first_day_of_the_month_in_timestamp(month)
            end_date = last_day_of_month_in_timestamp(month)

            stock_data = f'https://finance.yahoo.com/quote/{stock}/history?period1={start_date}&period2={end_date}&interval=1d&filter=history&frequency=1d'

            tables = pd.read_html(stock_data)
            table_list.append(tables)
            
        return table_list

    gold = stock_dataframes("GC%3DF")
    oil = stock_dataframes("CL%3DF")
    air_canada = stock_dataframes("AC.TO")

    jan_gold_df = gold[0][0]
    feb_gold_df = gold[1][0]
    mar_gold_df = gold[2][0]
    apr_gold_df = gold[3][0]
    may_gold_df = gold[4][0]
    jun_gold_df = gold[5][0]
    jul_gold_df = gold[6][0]
    aug_gold_df = gold[7][0]

    jan_oil_df = oil[0][0]
    feb_oil_df = oil[1][0]
    mar_oil_df = oil[2][0]
    apr_oil_df = oil[3][0]
    may_oil_df = oil[4][0]
    jun_oil_df = oil[5][0]
    jul_oil_df = oil[6][0]
    aug_oil_df = oil[7][0]

    jan_air_canada_df = air_canada[0][0]
    feb_air_canada_df = air_canada[1][0]
    mar_air_canada_df = air_canada[2][0]
    apr_air_canada_df = air_canada[3][0]
    may_air_canada_df = air_canada[4][0]
    jun_air_canada_df = air_canada[5][0]
    jul_air_canada_df = air_canada[6][0]
    aug_air_canada_df = air_canada[7][0]

    gold_df = [aug_gold_df, jul_gold_df, jun_gold_df, may_gold_df, apr_gold_df, mar_gold_df, feb_gold_df, jan_gold_df]
    gold_stock_df = pd.concat(gold_df)
    gold_stock_df['Date'] = pd.to_datetime(gold_stock_df['Date'], errors='coerce').copy()
    gold_stock_df.reset_index(inplace=True)
    gold_stock_df.drop(columns='index', inplace=True)
    gold_stock_df = gold_stock_df[gold_stock_df.Open!='*Close price adjusted for splits.**Adjusted close price adjusted for both dividends and splits.']
    gold_stock_df = gold_stock_df[gold_stock_df.Open!='-'].copy()
    GOLD_df = gold_stock_df[['Date','Open','Close*']].copy()
    GOLD_df.columns = ['Date','Gold_open','Gold_close']
    GOLD_df['Gold_open'] = GOLD_df['Gold_open'].astype('str', copy=True).astype('float', copy=True)
    GOLD_df['Gold_close'] = GOLD_df['Gold_close'].astype('str', copy=True).astype('float', copy=True)
    GOLD_df['Gold_pert_change'] = round(((GOLD_df['Gold_close']-GOLD_df['Gold_open'])/(GOLD_df['Gold_open']))*100,2)

    oil_df = [aug_oil_df, jul_oil_df, jun_oil_df, may_oil_df, apr_oil_df, mar_oil_df, feb_oil_df, jan_oil_df]
    oil_stock_df = pd.concat(oil_df)
    oil_stock_df['Date'] = pd.to_datetime(oil_stock_df['Date'], errors='coerce').copy()
    oil_stock_df.reset_index(inplace=True)
    oil_stock_df.drop(columns='index', inplace=True)
    oil_stock_df = oil_stock_df[oil_stock_df.Open!='*Close price adjusted for splits.**Adjusted close price adjusted for both dividends and splits.']
    oil_stock_df = oil_stock_df[oil_stock_df.Open!='-'].copy()
    OIL_df = oil_stock_df[['Date','Open','Close*']].copy()
    OIL_df.columns = ['Date','Oil_open','Oil_close']
    OIL_df['Oil_open'] = OIL_df['Oil_open'].astype('str', copy=True).astype('float', copy=True)
    OIL_df['Oil_close'] = OIL_df['Oil_close'].astype('str', copy=True).astype('float', copy=True)
    OIL_df['Oil_pert_change'] = round(((OIL_df['Oil_close']-OIL_df['Oil_open'])/(OIL_df['Oil_open']))*100,2)

    air_canada_df = [aug_air_canada_df, jul_air_canada_df, jun_air_canada_df, may_air_canada_df, apr_air_canada_df, mar_air_canada_df, feb_air_canada_df, jan_air_canada_df]
    air_canada_stock_df = pd.concat(air_canada_df)
    air_canada_stock_df['Date'] = pd.to_datetime(air_canada_stock_df['Date'], errors='coerce').copy()
    air_canada_stock_df.reset_index(inplace=True)
    air_canada_stock_df.drop(columns='index', inplace=True)
    air_canada_stock_df = air_canada_stock_df[air_canada_stock_df.Open!='*Close price adjusted for splits.**Adjusted close price adjusted for both dividends and splits.']
    air_canada_stock_df = air_canada_stock_df[air_canada_stock_df.Open!='-'].copy()
    AC_df = air_canada_stock_df[['Date','Open','Close*']].copy()
    AC_df.columns = ['Date','Air_Canada_open','Air_Canada_close']
    AC_df['Air_Canada_open'] = AC_df['Air_Canada_open'].astype('str', copy=True).astype('float', copy=True)
    AC_df['Air_Canada_close'] = AC_df['Air_Canada_close'].astype('str', copy=True).astype('float', copy=True)
    AC_df['Air_Canada_pert_change'] = round(((AC_df['Air_Canada_close']-AC_df['Air_Canada_open'])/(AC_df['Air_Canada_open']))*100,2)

    Stock_df = GOLD_df.merge(OIL_df,on="Date",how="inner").merge(AC_df, on="Date", how="inner")
    stock_table = Stock_df.to_html(index=False)

    return stock_table

def bank_of_canada():

    base_url = "https://www.bankofcanada.ca/valet"
    query = "/observations/FXUSDCAD/json"
    url = base_url + query
    response = requests.get(url)
    response_json = response.json()
    exchange_rate_df = pd.DataFrame(response_json['observations'])
    renamed_df = exchange_rate_df.rename(columns={"d": "Date"})
    renamed_df = renamed_df.drop(renamed_df[renamed_df.Date < '2020-01-01'].index)
    reindexed_df = renamed_df.set_index('Date')
    normalized_df = pd.json_normalize(reindexed_df['FXUSDCAD'])
    normalized_df["v"]= normalized_df["v"].astype('str', copy=True).astype('float', copy=True)
    reindexed_df["USDxCAD_ExchangeRates"] = list(normalized_df["v"])
    boc_df = reindexed_df.drop(columns = ["FXUSDCAD"])
    boc_table = boc_df.to_html(index=True)

    return boc_table

def covid_table():

    covid_df = pd.read_csv("Resources/owid-covid-data.csv")
    covid_df1 = covid_df[["continent","location","date","total_cases","new_cases"]]
    covid_df2 = covid_df1[(covid_df1['location']=='Canada') | (covid_df1['location']=='United States')]  
    covid_df3 = covid_df2[(covid_df2['date']>='2020-01-01') & (covid_df2['date']<='2020-08-12')] 
    covid_df4 = covid_df3[["continent","location","date","new_cases","total_cases"]]
    covid_df5 = covid_df4.rename(columns={"continent":"Continent","location":"Country", "date":"Date",                                      "new_cases":"Daily New Cases", "total_cases":"Total Cases"})
    covid_data = covid_df5.reset_index(drop=True)
    Covid_df = covid_data.groupby('Date')
    Covid_df = Covid_df.sum()

    covid_table = Covid_df.to_html(index=True)

    return covid_table

def scrape():
    boc = bank_of_canada()
    covid = covid_table()
    stock = stock_tables()

    covid_data = {'BOC':boc,
                'Covid_cases':covid,
                'Stocks_hist': stock,
                  }
    return covid_data

