# amazon-target-walmart-stock-analysis

## Group Members
Winnie(Yuxi Zhang)
Faith
Jodiann

## Companies and Tickers
Amazon: AMZN
Target: TGT
Walmart: WMT

## Analysis Period
January 1, 2020, to December 31, 2025.

## Business Question
How did the stock performance of Amazon, Target, and Walmart differ from 2020 to 2025, and what business events may explain their significant price movements?

## Reason for  s compete in retail but differ in their business
models and customer segments. Comparing them helps us investigate how their stock performance responds to company-specific events and shared market conditions.

## Structure
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

## Project Status
Repository setup is complete. Data collection and analysis are in progress.

Findings

## Item 1: Data Collection
The stock price data for Amazon, Target, and Walmart was successfully collected from 2020 to 2025. The  dataset provides the foundation for comparing the performance of the three companies and identifying important market trends.

## Item 2: Data Inspection
The data inspection results showed that the dataset was loaded correctly and contained the necessary information for analysis. Reviewing the data structure helped verify that the stock data was complete and ready for further analysis.

## Item 3: Return Analysis and Correlation
The correlation matrix shows that Amazon, Target, and Walmart had positive correlations, meaning their stock returns generally moved in the same direction. The strongest relationship was between Target and Walmart (0.409), while Amazon and Walmart had the weakest correlation (0.291). Since the correlations are positive but not very strong, the results suggest that while the companies were influenced by some of the same market conditions, company-specific factors such as earnings reports, inventory challenges, and changes in consumer spending also affected each stock differently. ``
