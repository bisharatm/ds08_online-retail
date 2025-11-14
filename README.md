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

This project focuses on customer segmentation analysis within e-commerce context that distinguishes UK and international buyers using purchasing frequency, recency, and spending patterns. The aim is to organize customers into meaningful groups that can guide market-specific marketing strategies, retention plans and commercial efforts.

We will work with transactional data from December 2010 to December 2011, address known issues such as missing CustomerID values, ambiguous cancellations or adjustments, and inconsistent descriptions, and engineer features that capture repeat purchase intervals such as the average days between purchases, recency in days, and monetary value. We will then apply unsupervised clustering, using K-means with an elbow-based check for the number of clusters.

The final deliverables will include clear segment definitions, behavioral profiles and actionable recommendations that support targeted campaigns and resource allocation. The specific business question, stakeholder groups, and risk considerations are detailed in the sections below.

#### Business Question:

- How do domestic (UK) and international customers cluster based on purchasing frequency, purchasing recency, and spending patterns in order to identify high-value customer groups and design targeted marketing strategies?

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

# Setup Instructions
1. Clone this repository (If this is a fork, use your fork's URL below).

    `git clone https://github.com/bisharatm/ds08_team-project.git`

2. Change to the project directory

    `cd ds08_online-retail`

3. Install dependencies

    **Note:** Create and activate a **seperate** virtual environment for the project.

    `pip install -r requirements.txt`

4. Launch Jupyter Notebook (dashboard opens in browser)

    `jupyter notebook`

5. Run notebooks

    Navigate to each notebook (numbered sequentially), open and run individually, making sure to run them in the intended order. Various outputs, such as, interim and final datasets, and visualizations will be exported and saved into approprirate folders under `data/` or `reports/`.