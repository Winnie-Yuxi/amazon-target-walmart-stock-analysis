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

#Work Item 3: Returns, descriptive statistics, and correlation
prices = prices.sort_values(['Ticker', 'Date']).copy()
prices['Daily_Return_Pct'] = prices.groupby('Ticker')['Close'].pct_change() * 100
print("--- Return distribution by ticker (count, mean, median, min, max, std) ---")
for ticker in prices['Ticker'].unique():     
    ticker_prices = prices[prices['Ticker'] == ticker]  
    best_day = ticker_prices.loc[ticker_prices['Daily_Return_Pct'].idxmax()]
    worst_day = ticker_prices.loc[ticker_prices['Daily_Return_Pct'].idxmin()]
    print(f"\n{ticker}: best day {best_day['Date'].date()} ({best_day['Daily_Return_Pct']:.2f}%), "
          f"worst day {worst_day['Date'].date()} ({worst_day['Daily_Return_Pct']:.2f}%)")

price_and_return_stats = (
    prices.groupby('Ticker')[['Close', 'Daily_Return_Pct']]
    .agg(['count', 'mean', 'median', 'min', 'max', 'std'])
)

# The result has hierarchical column labels: the measure (Close / Daily_Return_Pct) and then
# the statistic (mean / median / etc.). This keeps both measures and all six required statistics visible.
print("--- Closing price and daily return statistics by ticker ---")
print(price_and_return_stats)

# Align each stock's daily returns by date.
returns_wide = prices.pivot(
    index='Date',
    columns='Ticker',
    values='Daily_Return_Pct'
)

# Calculate correlations between the stocks' daily returns.
correlation = returns_wide.corr()

print("\n--- Daily return correlation matrix ---")
print(correlation.round(3))

# Work Item 4: Monthly average closing price by ticker
grouped = prices.groupby("Ticker").agg(
    avg_close=("Close", "mean"),
    avg_daily_return_pct=("Daily_Return_Pct", "mean"),
    median_daily_return_pct=("Daily_Return_Pct", "median"),
    return_std_pct=("Daily_Return_Pct", "std"),
    avg_volume=("Volume", "mean"),
)
# A second summary by time. resample is the time version of groupby.
monthly_avg_close = (
    prices.set_index("Date")
    .groupby("Ticker")["Close"]
    .resample("ME")
    .mean()
    .unstack("Ticker")
)

print("Last three months of average adjusted close:")
print(monthly_avg_close.tail(3))

# Work Item 5: Meaningful Period Returns
for ticker, ticker_data in prices.groupby("Ticker"):
    highest_return = ticker_data.sort_values(
        "Daily_Return_Pct", ascending=False
    ).iloc[0]
    lowest_return = ticker_data.sort_values(
        "Daily_Return_Pct", ascending=True
    ).iloc[0]

    print(ticker)
    print("Highest return:", highest_return)
    print("Lowest return:", lowest_return)

# Work Item 6: Visualizations
normalized.plot(figsize=(10, 6))
plt.title("Normalized price performance across the analysis period")
plt.xlabel("Date")
plt.ylabel("Indexed price (first observation = 100)")
plt.tight_layout()
plt.savefig("charts/normalized_prices.png", dpi=150)
plt.show()

movement_window = prices[
    prices["Date"].between("2023-03-01", "2023-04-15")
]

return_matrix.plot.box(figsize=(9, 5))
plt.title("Daily return distributions by ticker")
plt.xlabel("Ticker")
plt.ylabel("Daily return (%)")
plt.tight_layout()
plt.savefig("charts/return_distribution.png", dpi=150)
plt.show()
