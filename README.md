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
Stock price data for Amazon, Target, and Walmart was successfully collected from 2020 to 2025. This data provides the foundation for comparing the performance of the three companies.

## Item 2: Data Inspection
The dataset was reviewed to confirm that the data was complete, organized, and ready for analysis.

## Item 3: Return Analysis and Correlation
The correlation matrix shows that Amazon, Target, and Walmart had positive correlations, meaning their stock returns generally moved in the same direction. The strongest relationship was between Target and Walmart (0.409), while Amazon and Walmart had the weakest correlation (0.291). 

## Item 4: Monthly Average Closing Price Summary
The monthly average closing prices show how Amazon, Target, and Walmart performed over time. Amazon had the highest average stock price, while Walmart showed steady growth near the end of the period.
