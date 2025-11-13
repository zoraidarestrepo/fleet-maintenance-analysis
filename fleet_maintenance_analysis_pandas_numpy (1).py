
"""Fleet Maintenance Analysis using Pandas & NumPy

This script loads the FleetMaintenanceRecords dataset from either:
- A CSV file (FleetMaintenanceRecords.csv), or
- An Excel file (FleetMaintenanceRecords.xlsx / FleetMaintenanceRecords (2).xlsx)

It performs basic cleaning and exploratory analysis commonly used
in data analytics and reliability studies.
"""

import os
import numpy as np
import pandas as pd


def load_fleet_data():
    """Load fleet maintenance data from CSV or Excel.

    Priority:
    1. Excel: 'FleetMaintenanceRecords (2).xlsx'
    2. Excel: 'FleetMaintenanceRecords.xlsx'
    3. CSV:   'FleetMaintenanceRecords.csv'
    """
    candidates = [
        "FleetMaintenanceRecords (2).xlsx",
        "FleetMaintenanceRecords.xlsx",
        "FleetMaintenanceRecords.csv",
    ]

    for path in candidates:
        if os.path.exists(path):
            ext = os.path.splitext(path)[1].lower()
            if ext in [".xlsx", ".xls"]:
                print(f"Loading Excel file: {path}")
                df = pd.read_excel(path)
            else:
                print(f"Loading CSV file: {path}")
                df = pd.read_csv(path)
            return df, path

    raise FileNotFoundError(
        "No fleet maintenance file found. "
        "Expected one of: 'FleetMaintenanceRecords (2).xlsx', "
        "'FleetMaintenanceRecords.xlsx', 'FleetMaintenanceRecords.csv'."
    )


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: lowercase, replace spaces with underscores."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def summarize_by_repair_type(df: pd.DataFrame) -> pd.DataFrame:
    """Count repairs by repair_type with failure rate proxy."""
    if "repair_type" not in df.columns:
        print("Column 'repair_type' not found. Skipping repair-type summary.")
        return pd.DataFrame()

    summary = (
        df.groupby("repair_type")
        .agg(
            num_repairs=("repair_type", "size"),
            avg_cost=("repair_cost", "mean") if "repair_cost" in df.columns else ("repair_type", "size"),
        )
        .reset_index()
        .sort_values("num_repairs", ascending=False)
    )
    return summary


def summarize_by_state(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize failures by state (region-level view)."""
    if "state" not in df.columns:
        print("Column 'state' not found. Skipping state summary.")
        return pd.DataFrame()

    summary = (
        df.groupby("state")
        .agg(
            num_repairs=("state", "size"),
            unique_vehicles=("vehicle_id", "nunique") if "vehicle_id" in df.columns else ("state", "size"),
        )
        .reset_index()
        .sort_values("num_repairs", ascending=False)
    )
    return summary


def summarize_by_vehicle_year(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize failures by vehicle_year, using NumPy for some stats.

    This assumes there is a 'vehicle_year' column.
    """
    if "vehicle_year" not in df.columns:
        print("Column 'vehicle_year' not found. Skipping vehicle_year summary.")
        return pd.DataFrame()

    year_counts = df["vehicle_year"].value_counts().sort_index()
    years = year_counts.index.to_numpy()
    counts = year_counts.to_numpy()

    # Basic NumPy stats on failure counts per year
    stats = {
        "min_failures": int(np.min(counts)),
        "max_failures": int(np.max(counts)),
        "mean_failures": float(np.mean(counts)),
        "median_failures": float(np.median(counts)),
    }

    summary = pd.DataFrame(
        {
            "vehicle_year": years,
            "num_repairs": counts,
        }
    )

    print("Failure-count stats by vehicle_year (using NumPy):")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    return summary


def main():
    # 1. Load data from CSV/Excel
    df_raw, path_used = load_fleet_data()
    print(f"Loaded {len(df_raw):,} rows from: {path_used}\n")

    # 2. Clean column names
    df = clean_columns(df_raw)

    # 3. Basic info
    print("Columns:", list(df.columns))
    print("First 5 rows:")
    print(df.head(), "\n")

    # 4. Summaries
    repair_type_summary = summarize_by_repair_type(df)
    state_summary = summarize_by_state(df)
    vehicle_year_summary = summarize_by_vehicle_year(df)

    # 5. Save summaries to CSV for further use / Power BI / Excel
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    if not repair_type_summary.empty:
        repair_type_summary.to_csv(os.path.join(output_dir, "repair_type_summary.csv"), index=False)
        print("Saved repair_type_summary.csv")

    if not state_summary.empty:
        state_summary.to_csv(os.path.join(output_dir, "state_summary.csv"), index=False)
        print("Saved state_summary.csv")

    if not vehicle_year_summary.empty:
        vehicle_year_summary.to_csv(os.path.join(output_dir, "vehicle_year_summary.csv"), index=False)
        print("Saved vehicle_year_summary.csv")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
