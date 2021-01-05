# Finance-Yahoo-ETL


## Sources for Data Extraction
- Yahoo Finance historical stock price data: https://ca.finance.yahoo.com/quote/L.TO/history?p=L.TO

- European Centre for Disease Prevention and Control (ECDC) Covid-19 cases data: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide

- Identified the Bank of Canada Valet API: https://www.bankofcanada.ca/valet/docs as a reliable dataset to look at the financial impact of the COVID-19 pandemic through the indicator of the US <=> CAD Exchange Rate


## Method of Data Extraction
- **Yahoo Finance Data:**  
    - Pandas library was used to extract the data from Yahoo Finance website
    - A function was created to extract historical daily stock data of any stock by month to mitigate Yahoo Finance’s limit of 100 data points when scraping

- **Covid-19 Cases Data:**
    - Pandas library was used to read csv file downloaded from ECDC website

- **USD <=> CAD Exchange Rates:**
    - Jupyter Notebook was used to call the Bank of Canada Valet API
    - Used documentation to give the API call a specific query to pull the daily observations of the  US <=> CAD Exchange Rate in JSON format


## Data Transformation Process

- **Yahoo Finance Data:** 
    - We converted our list of monthly stock data into dataframes 
    - These dataframes were appended to a final dataframe for the stock that contains pricing information of the stock for 2020 
    - Filtered the stock dataframe to select the date, the open price, the close price. 
    - Converted the data types for the filtered dataframe 
    - Created a new column for the daily percentage changes 
    - Used an Inner-Join to consolidate  the individual stock dataframes
    - Set the “Date” column as the Index
	
- **Covid-19 Cases Data:**
    - Collected a list of all columns we need
    - Filtered data for only Canada & USA ,reorganize and rename the columns
    - Grouped the dataframe by Data to get the final dataframe
    - Set the “Date” column as the Index

- **USD x Canadian Exchange Rates:**
    - Converted the exchange rate JSON into a DataFrame
    - Renamed the columns
    - Filtered by selecting the specific timeframe desired (filtered to only show from 2020-01-01 to 2020-08-13)
    - Set the “Date” column as the Index
    - Normalized the column holding the exchange rate values as it was set to the dtype of object 
    - Replaced the non-normalized Exchange Rate Column with the normalized Exchange Rate column by adding and dropping columns
    - Achieved data in desired transformed state

## Data Loading Process

- Chose to use SQL (pgAdmin4), a relational database, to store our data
- Created a relationship diagram for our combined database (titled “covid_finance_db” (see script.sql)) through https://app.quickdatabasediagrams.com and exported the DB schema diagram to PostgreSQL
- Adjusted the column names in SQL to ensure they matched the column names for their associated tables that we had created previously in the Jupyter Notebook file
- Used Jupyter Notebook to connect our engine and uploaded data to SQL: COVID-Cases, USDxCAD_ExchangeRate and Stock_Dataframe into the three existing tables in a SQL database


### **Data has now been Extracted, Transformed and Loaded in!**



