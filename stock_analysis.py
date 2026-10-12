#Work Item 1: Confirm that the selected stock code can be downloaded
import os 
import yfinance as yf
import pandas as pd

TICKERS = ['AMZN', 'TGT', 'WMT']  
START_DATE = '2020-01-01' 
END_DATE = '2026-01-01'            
OUTPUT_DIR = 'outputs_group_assignment' 
raw = yf.download(TICKERS, start=START_DATE, end=END_DATE, auto_adjust=True, group_by='ticker')

# Confirm that data was downloaded.
if raw is None or raw.empty:
    raise ValueError("No data downloaded.")

print(raw.head())

# Check that every company has valid closing prices.
counts = pd.Series({t: raw[t]['Close'].count() for t in TICKERS})

print("\nValid closing prices for each stock:")
print(counts)

if (counts == 0).any():
    raise ValueError("At least one stock failed to download.")

print("\nAll three stocks downloaded successfully.")

#Work Item 2: Load and inspect the data
frames = []  
for ticker in TICKERS:
    ticker_frame = raw[ticker].copy()   
    ticker_frame['Ticker'] = ticker 
    frames.append(ticker_frame)  

prices = pd.concat(frames).reset_index()

print(f"Tickers: {TICKERS}")
print(f"Date range: {prices['Date'].min().date()} to {prices['Date'].max().date()}") 
print(f"Records: {len(prices):,}")               
print(f"Columns: {prices.columns.tolist()}")     
print(f"Dtypes:\n{prices.dtypes}")              
print("\n--- Missing values by column ---")
print(prices.isna().sum().sort_values(ascending=False))