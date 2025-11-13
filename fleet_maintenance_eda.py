# fleet_maintenance_eda.py / Notebook Cell 1
import pandas as pd
import numpy as np

# Display options (optional, for nicer tables)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

# Load data
df = pd.read_csv("FleetMaintenanceRecords.csv")

print("First 5 rows:")
display(df.head())

print("\nDataFrame info:")
df.info()

print("\nSummary statistics (numeric columns):")
display(df.describe())

# Notebook Cell 2 – Cleaning & Preparation

# Standardize column names to snake_case
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Example common column names – adjust if yours are slightly different
# Assume columns like: state, part_name, event_type, event_date, cost, vehicle_id
# Parse dates
if "event_date" in df.columns:
    df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")

# Strip whitespace from string columns
str_cols = df.select_dtypes(include="object").columns
for col in str_cols:
    df[col] = df[col].str.strip()

# Drop exact duplicate rows
df = df.drop_duplicates()

# Optional: drop rows with no state or part_name
required_cols = [col for col in ["state", "part_name", "event_type"] if col in df.columns]
df = df.dropna(subset=required_cols)

# Notebook Cell 3 – Basic Overview

print("States:", df["state"].nunique() if "state" in df.columns else "no 'state' column")
print("Parts:", df["part_name"].nunique() if "part_name" in df.columns else "no 'part_name' column")
print("Event types:", df["event_type"].nunique() if "event_type" in df.columns else "no 'event_type' column")

if "event_date" in df.columns:
    print("Date range:", df["event_date"].min(), "→", df["event_date"].max())

# Notebook Cell 4 – Frequency Analysis

if "part_name" in df.columns:
    print("\nTop 10 most frequently serviced/replaced parts:")
    display(df["part_name"].value_counts().head(10))

if "state" in df.columns:
    print("\nTop 10 states by maintenance events:")
    display(df["state"].value_counts().head(10))

if "event_type" in df.columns:
    print("\nEvent type distribution:")
    display(df["event_type"].value_counts())

# Notebook Cell 5 – Time Trend Analysis

if "event_date" in df.columns:
    # Ensure sorted by date
    df = df.sort_values("event_date")

    # Events per month
    events_per_month = (
        df.set_index("event_date")
          .resample("M")
          .size()
          .rename("event_count")
          .reset_index()
    )

    print("\nEvents per month (first 12 rows):")
    display(events_per_month.head(12))

# Notebook Cell 6 – State x Part Analysis

if {"state", "part_name"}.issubset(df.columns):
    state_part_counts = (
        df.groupby(["state", "part_name"])
          .size()
          .reset_index(name="event_count")
          .sort_values("event_count", ascending=False)
    )

    print("Top 20 state–part combinations by event count:")
    display(state_part_counts.head(20))

# Notebook Cell 7 – Cost Analysis (optional)

if "cost" in df.columns:
    print("\nTotal maintenance cost:", df["cost"].sum())
    print("Average cost per event:", df["cost"].mean())

    if "state" in df.columns:
        cost_by_state = (
            df.groupby("state")["cost"]
              .agg(["count", "sum", "mean"])
              .sort_values("sum", ascending=False)
        )
        print("\nCost by state:")
        display(cost_by_state.head(10))

# Notebook Cell 8 – Visualizations
import matplotlib.pyplot as plt

# Top 10 parts
if "part_name" in df.columns:
    top_parts = df["part_name"].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    top_parts.plot(kind="bar")
    plt.title("Top 10 Most Frequently Serviced Parts")
    plt.xlabel("Part Name")
    plt.ylabel("Number of Events")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

# Events per month
if "event_date" in df.columns:
    events_per_month.set_index("event_date", inplace=True)

    plt.figure(figsize=(10, 5))
    events_per_month["event_count"].plot()
    plt.title("Maintenance Events Over Time (Monthly)")
    plt.xlabel("Month")
    plt.ylabel("Number of Events")
    plt.tight_layout()
    plt.show()

print("Shape after cleaning:", df.shape)
