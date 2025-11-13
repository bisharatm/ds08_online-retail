# Domestic (UK) and International customer purchasing behavior
Data Sciences Institute - Cohort 7 - Team DS08 - Final Project

# Members
* Ayesha Hasan
* Bisharat Memon
* Jose Sosa

# Project Overview

* [Project Scope and Objectives](#project-scope-and-objectives)
* [Methodology](#methodology)
    * [Process](#process)
    * [Raw Data Inspection](#raw-data-inspection)
    * [Data Cleaning](#data-cleaning)
    * [Exploratory Data Analysis](#exploratory-data-analysis)
    * [Modeling: Clustering and Segmentation](#modeling-clustering-and-segmentation)
    * [Visualizations and Insights](#visualizations-and-insights)
    * [Conclusion and Recommendations](#conclusion-and-recommendations)
* [Team Videos](#team-videos)

Raw data source: [UC Irvine Machine Learning Repository - Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)

Features of Interest: Quantity, InvoiceDate, UnitPrice, CustomerID, Country

# Project Scope and Objectives

This project focuses on analysing customer purchasing behaviour within an e-commerce context, with a particular emphasis on comparing domestic (UK) buyers and international buyers. By examining purchasing frequency, recency, and spending patterns, the aim is to group customers into meaningful behavioural segments that can support market-specific marketing strategies, customer retention initiatives, and broader commercial planning.

Using transactional data from December 2010 to December 2011, the project addresses several known data challenges, including missing CustomerID values, ambiguous cancellation records, and inconsistent item descriptions. Additional engineered variables, such as average days between purchases, recency in days, and total monetary value, create a richer foundation for behavioural analysis. These prepared features will then be used for unsupervised clustering through K-means, with the final number of clusters validated using elbow-based techniques.

The outcome of this work is a set of well-defined customer segments, accompanied by behavioural profiles and actionable recommendations. These insights are designed to support targeted campaigns, inform strategic decision-making, and optimise commercial resource allocation.

#### Business Case and Analytical Focus

The central goal of the analysis is to understand how customer behaviour differs between the UK and international markets and how these differences translate into value for the business. While the UK constitutes the majority of transactions, international customers may demonstrate distinct, potentially high-value purchasing patterns that warrant tailored engagement. By revealing these behavioural differences, the project provides the organisation with evidence to support differentiated marketing strategies rather than a one-size-fits-all approach.

#### Business Question:

- How do domestic (UK) and international customers cluster based on purchasing frequency, purchasing recency, and spending patterns in order to identify high-value customer groups and design targeted marketing strategies?

This question anchors the analytical approach and ensures that the segmentation directly supports relevant commercial decisions.

#### Stakeholders:

- Business Development Team: Use customer clusters to identify priority markets, forecast sales by group, and plan partnerships and channel investments.
- Marketing and Customer Insights Team: Translate customer profiles into tailored offers, communication plans and engagement strategies, and track results to improve future campaigns.
- Data Science/Analytics Team: Maintain data pipeline, update segmentation when needed, and produce dashboards for decision support and ongoign monitoring.

#### Risks and uncertainties:

- Uncertainties: 
    1. Having insufficient sample size, especially for international markets, may affect cluster representativeness.
    2. Ambiguity in cancellation reasons.
    3. Dataset spans December 2010 to December 2011, a single year, only therefore, external factors such as economic conditions, seasonality, and promotional cycles may impact generalizability for future years.
    4. Other factors not accounted for in dataset directly, such as delivery times, customer service experience, and online purchasing experience.

- Risks:
    1. Identified target segments may not be substantial in size or business impact.
    2. Insights may be biased due to missing or insufficient data.

# Methodology

#### Process:

- Raw data Inspection: Audit schema and coverage, check date ranges, duplicates, cancellations, and country distribution to confirm data readiness.
- Data Cleaning: Prepare a single analysis-ready file, handle missing values, correct data types and standardize labels of interest; flag cancellations and adjustments, deduplicate and compute reliable totals.
- Exploratory Data Analysis: Summarize and compare the UK versus international mix, purchase frequency, recency, and spend, check for outliers and seasonality.
- Modeling: Clustering and Segmentation: Engineer frequency, recency, and spend features, scale data, run K-means, select k via elbow and silhouette method, and label segments.
- Visualizations and Insights: Create clear plots and summaries illustrating segment size, value, and behaviors by market for stakeholders.
- Conclusion and Recommendations: Synthesize segment findings into actionable recommendations for targeted marketing strategies and next steps, noting limitations and assumptions.

#### Technical Stack:

- VS Code
- Slack
- Google Docs
- Google Colab
- Zoom Meetings 

#### Programming Languages:

- Python

#### Libraries Used:

- Data Analysis and Visualization:
    1.  numpy
    2.  pandas
    3.  matplotlib
    4.  datatime
    5.  seaborn

- Clustering model, Evaluation and Validation:
    1.  scikit-learn

## Raw data Inspection

The project begins with a controlled and reproducible process to fetch the original Online Retail dataset from the UC Irvine Machine Learning Repository. Instead of relying on manual downloads, the team uses a small, automated pipeline that ensures everyone works from the same trusted source.

The notebook loads configuration values from a .env file, including the remote data URL and the local raw data directory. A dedicated utility function then downloads the dataset as a ZIP file, stores it in the raw data folder, and extracts its contents for use in subsequent steps.

#### This approach delivers three main benefits:

- Consistency across the team: All collaborators access the exact same data from a single, versioned source.

- Reproducibility: The entire raw data acquisition process can be rerun at any time with a single command, supporting transparent and repeatable analysis.

- Clear data lineage: Separating raw data into a dedicated directory makes it easy to distinguish original files from any cleaned or transformed outputs used later in the project.

By formalizing the data fetch into code, the project establishes a stable foundation for the downstream cleaning, exploration, and clustering work.

## Data Cleaning

This stage transforms the raw Online Retail dataset into a reliable, analytics-ready table by addressing missing information, correcting structural inconsistencies, and standardizing key identifiers. The goal is to ensure that every transaction used in the segmentation model represents a valid, attributable customer purchase across clearly defined markets.

We began by importing the original Excel file and writing it to an intermediate CSV. Because CSV files do not preserve data types, the project uses an external source file that defines the expected schema for all key fields including invoice number, product code, description, quantity, unit price, customer ID, and country. This shared schema is referenced across all notebooks so that each dataset is read with consistent data types, supporting a fully reproducible and transparent pipeline.

A series of systematic checks were then performed to assess and improve data quality:

#### 1. Missing values and unusable records
The exploratory checks confirmed that missing values were concentrated in the Description and CustomerID fields, with the largest share originating from the United Kingdom. Since transactions without a customer ID cannot support customer-level analysis and transactions without a description lack product attribution, all rows missing either field were removed. This ensures that recency, frequency, and monetary calculations are based solely on complete and traceable customer activity.

#### 2. Duplicate transactions and invalid quantities or prices
The dataset contained more than five thousand fully duplicated rows, which were removed to avoid inflating purchase counts. Additional inspection revealed negative quantities and zero prices, typically associated with cancellations or administrative adjustments. These values were excluded to retain only revenue-generating purchases and avoid distortions in customer spending profiles.

#### 3. Data type corrections for analytical consistency
Using the shared schema definition, the InvoiceDate field was converted to a datetime format to enable accurate time-based feature engineering. Other categorical fields including invoice number, stock code, country, product description, and customer ID were standardized to string types so that grouping, filtering, and joins behave consistently across the analysis workflow.

#### 4. Standardizing country labels
Country names were cleaned to eliminate inconsistent spacing, unify text casing, and expand acronyms such as EIRE to Ireland, RSA to South Africa, and USA to United States. Non-geographic placeholders including "Unspecified" and "European Community" were removed to ensure that every transaction is linked to a clearly identifiable country.

Following these steps, the dataset was reduced from more than half a million records to approximately 392,000 high-quality, customer-attributable transactions. This curated dataset forms the foundation for the exploratory analysis and clustering that follows and ensures that the resulting customer segments are grounded in well-defined and reliable transactional behavior.

## Exploratory Data Analysis

The exploratory analysis focused on understanding customer behaviour across domestic and international markets while preparing the dataset for segmentation. After enforcing consistent data types using the project’s central schema file, several engineered features were introduced to support deeper behavioural insights.

Preparation steps included:

- Validating and converting data types according to the external schema definition
- Creating a transaction-level revenue field
- Flagging cancelled orders based on invoice patterns
- Classifying all customers into domestic or international segments
- Saving cleaned, structured and enriched data into the project’s organised data directories

Initial analysis revealed clear differences between markets. Domestic customers account for most transactions, while international customers place fewer orders but spend more per purchase. Weekly activity patterns show that:

- Domestic orders occur frequently and consistently
- International orders appear less often
- Revenue spikes from international customers tend to be larger due to higher-value baskets

This contrast is shown below.

![Weekly Orders and Revenue (Domestic vs International)](reports/eda/trend_weekly_orders_revenue_split.png)

A wider commercial snapshot confirms the distinct dynamics of each customer base. Comparing total orders, total revenue and Average Order Value (AOV) across regions shows:

#### * Domestic customers:
    * Represent the majority of order volume
    * Generate most of the total revenue
    * Maintain lower average order values

#### * International customers:
    * Account for a smaller proportion of orders
    * Contribute a meaningful share of revenue despite lower volume
    * Exhibit significantly higher average order values

These differences are summarised in the following visualization.

![Market Snapshot: Orders, Revenue, and AOV](reports/eda/market_snapshot_orders_revenue_aov.png)

From the Monthly Average Order Value trends, a clear separation is observed for most of the year, with international customers consistently placing higher-value orders than domestic buyers. This pattern shifts at the end of the year. In December, the two markets converge, with the international AOV decreasing and the domestic AOV increasing, resulting in both groups showing similar order values for the first time in the annual cycle. This equalisation suggests a seasonal effect in which UK customers increase spending ahead of the holidays while international order values temporarily contract.

![Monthly Average Order Value by Market](reports/eda/monthly_aov_by_market.png)

To support segmentation, Recency, Frequency and Monetary metrics were engineered at the customer level. These features capture core dimensions of purchasing behaviour:

- Recency measures days since the most recent purchase
- Frequency counts the number of unique transactions
- Monetary represents total customer spend

Final preparation work included:

- Merging the RFM metrics with customer attributes such as country and region
- Creating separate domestic and international datasets for modelling
- Exporting all RFM outputs to the prepared data folder for reproducibility

Overall, the exploratory analysis highlights two structurally different customer groups. Domestic customers form a high-volume, stable purchasing base, while international customers contribute less frequently but with higher-value orders. These insights, together with the engineered RFM dataset, establish a strong analytical foundation for the subsequent clustering and segmentation stage.

## Modeling: Clustering and Segmentation

## Visualizations and Insights

## Conclusion and Recommendations

# Team Videos

* Ayesha Hasan |
* Bisharat Memon |
* Jose Sosa |

