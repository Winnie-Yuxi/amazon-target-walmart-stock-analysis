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

## Item 4: Monthly and Annual Average Closing Price Summary
We used pandas 'groupby()' and 'resample()' to calculate the monthly and annual average adjusted closing prices of Amazon, Target, and Walmart from 2020 to 2025.
The results reveal different long-term trends. Amazon experienced a noticeable decline in 2022 followed by a recovery, while Walmart showed a generally upward trend in later years. Target experienced significant fluctuations and weaker performance toward the end of the analysis period.
These findings help us compare the companies' historical stock price trends and understand how their performance differed over time.
The complete monthly and annual summary tables are available in the 'outputs_group_assignment' folder.

## Item 5: Significant Stock Movements and Business Events

### Overview

Our analysis identified significant daily stock price movements for Amazon (AMZN), Target (TGT), and Walmart (WMT) between 2020 and 2025. We focused on three major declines in April and May 2022 to investigate how financial performance, rising operating costs, and inflation affected investor confidence.

### Amazon (AMZN) — April 29, 2022

Amazon experienced a significant daily return of **-14.05%** on April 29, 2022. This decline followed the company's disappointing first-quarter earnings report. Amazon faced rising operating costs, slower growth, and concerns about its future profitability. The company also reported a quarterly net loss, partly related to its investment in Rivian.

These results raised investor concerns about Amazon's ability to maintain strong profitability during a period of economic uncertainty.

### Walmart (WMT) — May 17, 2022

Walmart experienced a daily return of **-11.38%** on May 17, 2022. The company reported a decline in quarterly earnings and lowered its annual profit forecast.

Rising fuel, transportation, and labor costs reduced profitability. At the same time, inflation affected consumer purchasing behavior, as customers increasingly focused on essential products with lower profit margins.

This event demonstrates how increasing operating expenses can negatively affect a retailer's profitability and stock performance.

### Target (TGT) — May 18, 2022

Target experienced a sharp daily return of **-24.93%** on May 18, 2022, representing its largest daily decline in our dataset.

The company reported that its first-quarter profit had fallen by approximately half. Higher transportation and fuel costs, along with inflation-related pressures, significantly reduced its profit margins.

Investors reacted negatively to the disappointing earnings results and concerns about future profitability, leading to a major decline in Target's stock price.

### Business Analysis and Conclusion

These three events demonstrate how inflation, rising operating costs, and disappointing financial results can affect stock prices.

Walmart and Target experienced particularly significant declines on consecutive trading days in May 2022, suggesting that both companies faced similar challenges in the retail industry.

Amazon also experienced a major decline during the same broader period of economic uncertainty, although its business model and financial challenges differed from those of Walmart and Target.

Overall, our findings suggest that investors should consider not only revenue growth but also operating costs, profitability, and broader economic conditions when evaluating companies.

### References

- Amazon.com, Inc. (2022, April 28). *Amazon announces first quarter results.*
- Reuters. (2022, April 29). *Wall Street closes sharply lower on Amazon slump, inflation worries.*
- Reuters. (2022, May 17). *Walmart profit falls short, cuts outlook, hit by higher fuel and labor costs.*
- Reuters. (2022, May 18). *Wall Street ends sharply lower as Target and growth stocks sink.*

## Item 6: Stock Price Visualizations

### Figure 1: Normalized Stock Price Performance (2020–2025)

![Normalized Stock Prices](charts/normalized_prices.png)

This chart compares the relative stock price performance of Amazon, Target, and Walmart over the full analysis period, helping investors identify differences in long-term growth.

### Figure 2: Stock Price Movements (May–June 2022)

![Important Stock Movements](charts/important_movement.png)

This chart focuses on the significant stock price declines of Walmart and Target in May 2022, highlighting the impact of earnings disappointments and rising operating costs on major retailers.

### Figure 3: Daily Return Distributions

![Daily Return Distributions](charts/return_distribution.png)

This box plot compares daily return volatility across the three stocks, showing that Amazon and Target experienced greater fluctuations than Walmart during the analysis period.

### Figure 4: Daily Return Relationship Between AMZN and TGT

![Daily Return Relationship](charts/return_relationship.png)

This scatter plot shows a positive but relatively weak relationship between Amazon and Target's daily returns (r = 0.359), helping investors understand the degree to which their stock movements are related.

