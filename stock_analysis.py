import yfinance as yf

tickers = ["AMZN", "TGT", "WMT"]
raw = yf.download(
    tickers,
    start="2020-01-01",
    end="2026-01-01",
    auto_adjust=True,
    group_by="column",
    progress=False
)

# Confirm that data was downloaded.
if raw is None or raw.empty:
    raise ValueError("No data downloaded.")

print(raw.head())

# Check that every company has valid closing prices.
counts = raw["Close"].reindex(columns=tickers).count()

print("\nValid closing prices for each stock:")
print(counts)

if (counts == 0).any():
    raise ValueError("At least one stock failed to download.")

print("\nAll three stocks downloaded successfully.")