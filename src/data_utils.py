# Centralized loading and coercing data type helper
# Import relevant libraries
import pandas as pd

# Apply your standard dtype fixes for CSV's
def standardize_online_retail_dtypes(df):

    # InvoiceDate to datetime
    if "InvoiceDate" in df.columns:
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Selected columns to string
    cols_str = ["InvoiceNo", "StockCode", "Description", "Country", "CustomerID"]
    for col in cols_str:
        if col in df.columns:
            df[col] = df[col].astype("string")

    # Clean up CustomerID; remove ".0" suffix and "nan" to "NA"
    if "CustomerID" in df.columns:
        df["CustomerID"] = (
            df["CustomerID"]
            .astype("string")
            .str.replace(r"\.0$", "", regex=True)
            .replace("nan", pd.NA)
        )