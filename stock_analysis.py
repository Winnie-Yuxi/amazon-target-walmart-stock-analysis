#Work Item 1: Confirm that the selected stock code can be downloaded
import os 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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

# Work Item 4: Grouping and Time-Based Summary
# Overall summary for each stock
grouped = prices.groupby("Ticker").agg(
    avg_close=("Close", "mean"),
    avg_daily_return_pct=("Daily_Return_Pct", "mean"),
    median_daily_return_pct=("Daily_Return_Pct", "median"),
    return_std_pct=("Daily_Return_Pct", "std"),
    avg_volume=("Volume", "mean"),
)

print("\n--- Overall Summary by Ticker ---")
print(grouped.round(2).to_string())

# Calculate monthly average closing prices
monthly_avg_close = (
    prices.set_index("Date")
    .groupby("Ticker")["Close"]
    .resample("ME")
    .mean()
    .unstack("Ticker")
)

# Display the first and last 3 months
print("\n--- First 3 Months ---")
print(monthly_avg_close.head(3).round(2))

print("\n--- Last 3 Months ---")
print(monthly_avg_close.tail(3).round(2))

# Calculate annual average closing prices
annual_avg_close = monthly_avg_close.resample("YE").mean()
annual_avg_close.index = annual_avg_close.index.year

print("\n--- Annual Average Closing Prices ---")
print(annual_avg_close.round(2).to_string())

# Save complete tables to CSV
os.makedirs(OUTPUT_DIR, exist_ok=True)
grouped.to_csv(os.path.join(OUTPUT_DIR, "overall_summary.csv"))
monthly_avg_close.to_csv(os.path.join(OUTPUT_DIR, "monthly_average_close.csv"))
annual_avg_close.to_csv(os.path.join(OUTPUT_DIR, "annual_average_close.csv"))

# Work Item 5: Significant Stock Movements and Business Events
# Important dates identified from our return analysis
events = {"AMZN": "2022-04-29", "WMT": "2022-05-17", "TGT": "2022-05-18"}

print("\n--- Significant Stock Movements ---")
for ticker, event_date in events.items():
    event_data = prices[
        (prices["Ticker"] == ticker) &
        (prices["Date"] == event_date)
    ]

    print(f"\n{ticker} - {event_date}")
    print(event_data[["Date", "Close", "Daily_Return_Pct"]].to_string(index=False))

# Compare returns during the May 2022 retail earnings events
event_window = prices[prices["Date"].between("2022-05-16", "2022-05-20")]
event_returns = event_window.pivot(
    index="Date",
    columns="Ticker",
    values="Daily_Return_Pct"
)
print("\n--- May 2022 Retail Earnings Events ---")
print(event_returns.round(2).to_string())

# Save the event returns
event_returns.to_csv(os.path.join(OUTPUT_DIR, "may_2022_event_returns.csv"))

# Work Item 6: Visualizations
# Create a folder to save all charts
os.makedirs("charts", exist_ok=True)

## Chart 1: Normalized price performance across the full period
close_prices = prices.pivot(index="Date", columns="Ticker", values="Close")

normalized = close_prices / close_prices.iloc[0] * 100

normalized.plot(figsize=(10, 6))
plt.title("Normalized Stock Price Performance (2020-2025)")
plt.xlabel("Date")
plt.ylabel("Indexed Price (First Observation = 100)")
plt.legend(title="Ticker")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/normalized_prices.png", dpi=150)
plt.show()


## Chart 2: Zoomed-in view of an important movement period
# TGT and WMT experienced large daily declines in May 2022
movement_window = prices[
    prices["Date"].between("2022-05-01", "2022-06-15")
]
movement_prices = movement_window.pivot(index="Date", columns="Ticker", values="Close")

movement_prices.plot(figsize=(10, 6))
plt.title("Stock Price Movements: May-June 2022")
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price (USD)")
plt.legend(title="Ticker")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/important_movement.png", dpi=150)
plt.show()


## Chart 3: Daily return distributions by ticker
returns_wide.plot.box(figsize=(9, 5))
plt.title("Daily Return Distributions by Ticker")
plt.xlabel("Ticker")
plt.ylabel("Daily Return (%)")
plt.tight_layout()
plt.savefig("charts/return_distribution.png", dpi=150)
plt.show()


## Chart 4: Daily return relationship between AMZN and TGT
plt.figure(figsize=(7, 5))
plt.scatter(
    returns_wide["AMZN"],
    returns_wide["TGT"],
    alpha=0.35
)

plt.title("Daily Return Relationship: AMZN vs. TGT")
plt.xlabel("AMZN Daily Return (%)")
plt.ylabel("TGT Daily Return (%)")
plt.tight_layout()
plt.savefig("charts/return_relationship.png", dpi=150)
plt.show()
