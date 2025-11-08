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

This project defines the scope and objectives for a customer segmentation analysis that distinguishes UK and international buyers using purchasing frequency, recency, and spending patterns. The aim is to organize customers into meaningful groups that can guide market-specific marketing and commercial efforts.

We will work with transactional data from December 2010 to December 2011, address known issues such as missing CustomerID values, ambiguous cancellations or adjustments, and inconsistent descriptions, and engineer features that capture repeat purchase intervals such as the average days between purchases, recency in days, and monetary value. We will then apply unsupervised clustering, using K-means with an elbow-based check for the number of clusters.

The outputs will be clear segment definitions and profiles that support targeted campaigns and resource allocation. The specific business question, stakeholder groups, and risk considerations are detailed in the sections below.

#### Business Question:

- How do domestic (UK) and international customers cluster based on purchasing frequency, purchasing recency, and spending patterns in order to identify high-value customer groups and design targeted marketing strategies?

#### Stakeholders:

- Business Development Team: Could use the customer groups to decide which markets to focus on, estimate potential sales by group, and plan partnerships and channels.
- Marketing and Customer Insights Team: Might turn the group profiles into tailored offers and messages, adjust when and how people are contacted, and track results to improve future campaigns.
- Data Science/Analytics Team: May prepare and update the data, rerun the grouping when needed, and share clear summaries and dashboards so others can apply the findings.

#### Risks and uncertainties:

- Uncertainties: 
    i.      Having sufficient data, especially for international markets, to assess whether clusters are representative.
    ii.     Ambiguity in cancellation reasons.
    iii.    Data spans December 2010 to December 2011 only. External factors such as economic conditions, seasonality, and promotional cycles may have influenced purchasing and cancellation behavior, so findings
            should be generalized cautiously to future years.
    iv.     Other factors not modeled directly, such as delivery times, customer service experience, and online purchasing experience.

- Risks:
    i.      Target segments may not be substantially present in the customer base.
    ii.     Insights may be biased due to insufficient data.

# Methodology

#### Process:

- Raw data Inspection: audit schema and coverage, check date ranges, duplicates, returns, and country mix to confirm data fitness.
- Data Cleaning: prepare a single analysis-ready file, fix missing values, correct types and standardize leabels of interest; flag returns and adjustments, deduplicate and compute reliable totals.
- Exploratory Data Analysis: summarize the UK versus international mix, profile frequency, recency, and spend, check outliers and seasonality.
- Modeling: Clustering and Segmentation: engineer frequency, recency, and spend features, scale data, run K-means, select k via elbow and silhouette, and label segments.
- Visualizations and Insights: create clear plots and summaries that explain segment size, value, and behaviors by market for stakeholder consumption.
- Conclusion and Recommendations: synthesize segment findings into actionable targeting guidance and next steps, noting limitations and assumptions.

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
    i.      numpy
    ii.     pandas
    iii.    matplotlib
    iv.     datatime
    v.      seaborn

- Clustering model, Evaluation and Validation:
    i.      scikit-learn

## Raw data Inspection

## Data Cleaning

## Exploratory Data Analysis

## Modeling: Clustering and Segmentation

## Visualizations and Insights

## Conclusion and Recommendations

# Team Videos

