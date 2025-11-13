# Fleet Maintenance Analysis

### Overview

Analyzed fleet maintenance records using MySQL to identify part failure trends, regional performance issues, and cost drivers. Performed data cleaning, JOIN operations, and aggregations, then visualized insights in Excel/Power BI to support predictive maintenance decisions.

### Data Sources:

CSV dataset of fleet maintenance logs including part IDs, service timestamps, mileage, and regional repair data.

### Tools:

- MySQL — Imported and queried the fleet maintenance dataset [Download Here](https://github.com/user-attachments/files/23528910/fleet_maintenance_schema.sql)
  
- Python (Pandas, NumPy) — Data cleaning, transformation, and trend analysis [Download Here](https://github.com/user-attachments/files/23529746/fleet_maintenance_analysis_pandas_numpy.1.py)
  
- Excel — Initial data inspection and verification [Download Here](https://github.com/user-attachments/files/23528645/FleetMaintenanceRecords.xlsx)

- Power BI — Visualized part failures, regional trends, and maintenance patterns
  
- Jupyter Notebook — Environment for exploratory and statistical analysis [Download Here](https://github.com/user-attachments/files/23532753/FleetMaintenance_Analysis.ipynb)

## Data Cleaning & Preparation

Before analysis, the **FleetMaintenanceRecords** dataset was cleaned and standardized to ensure accuracy and consistency across all tools (Excel, MySQL, Python, Power BI):

1. **Loaded Raw Data**
   - Imported `FleetMaintenanceRecords.csv` / `.xlsx` into Excel, MySQL, and Python (pandas).
   - Verified row counts and column names matched across all environments.

2. **Standardized Column Names**
   - Renamed columns to use clear, consistent, and code-friendly names (e.g., `State`, `PartName`, `EventType`, `EventDate`).
   - Removed extra spaces and special characters from headers.

3. **Handled Missing & Invalid Values**
   - Checked for blank cells and `NULL` values in key fields (state, part name, event type, event date).
   - Removed rows with critical missing information that could not be reliably inferred.
   - Validated event counts and date formats; corrected obvious data entry errors where possible.

4. **Data Type Formatting**
   - Converted date fields to proper date/datetime types.
   - Ensured numeric fields (e.g., counts, mileage, cost if present) were stored as numeric types, not text.
   - Standardized categorical values (e.g., consistent state abbreviations, part names, and event types).

5. **Feature Preparation for Analysis**
   - Created summary tables for:
     - **Events by state**
     - **Events by part name**
     - **Events by event type / reason**
   - Aggregated counts using GROUP BY in MySQL and `groupby()` in pandas for further visualization and reporting.

These steps ensured the dataset was clean, consistent, and ready for analysis in Python, Excel pivot tables, SQL queries, and Power BI dashboards.

## Exploratory Data Analysis (EDA)

After cleaning and preparing the Fleet Maintenance dataset, exploratory data analysis (EDA) was performed using Python (pandas, NumPy), MySQL queries, Excel PivotTables, and Power BI. The goal was to uncover trends in part failures, maintenance activity, and regional patterns.

### 1. Dataset Overview
- Reviewed total number of maintenance records.
- Identified key variables such as:
  - **State**
  - **Part Name**
  - **Event Type**
  - **Event Date**
- Examined the distribution of events across time and locations.

### 2. Frequency Analysis
- Calculated the most frequently replaced parts.
- Determined the states with the highest number of maintenance events.
- Counted event types (e.g., inspections, repairs, replacements).

### 3. Trend Analysis
- Analyzed maintenance events over time to check for:
  - Seasonal patterns
  - Monthly/annual spikes in failures
  - Increases or decreases in maintenance activity

### 4. State-Level Breakdown
- Aggregated events by **state** to identify:
  - Regions with unusually high part failures
  - Areas requiring additional preventive maintenance resources

### 5. Part Failure Patterns
- Grouped by **Part Name** to identify:
  - Components most likely to fail
  - Any batch-specific or recurring issues
- Compared high-failure parts across states to detect localized trends.

### 6. Event Type Distribution
- Visualized how many events belonged to each category:
  - Repairs  
  - Replacements  
  - Inspections  
  - Service checks  
- Determined which event types are driving the majority of maintenance workload.

### 7. Correlations & Insights
- Looked for relationships such as:
  - States with higher event counts also having frequent failures of specific parts.
  - Certain months showing spikes in repairs (weather-related patterns).
  - Parts with consistent recurring issues indicating long-term reliability problems.

### 8. Visualizations (Python & Power BI)
- Created:
  - Bar charts of top failing parts
  - State-by-state maintenance heatmaps
  - Time-series plots of maintenance activity
  - Event type distribution charts
- Used these visuals to highlight actionable insights for operations teams.

### Summary of Findings
- **Certain parts** failed significantly more often than others, indicating potential design or usage issues.
- **Specific states** had disproportionately high maintenance events, suggesting environmental or operational factors.
- **Maintenance activity trends** showed identifiable seasonal or monthly spikes.

The EDA phase provided a clear picture of the dataset and guided the deeper analysis performed in Python, SQL, and Power BI.

### Data Analysis

This analysis explores maintenance patterns, part failures, and operational trends across a fleet of vehicles using the FleetMaintenanceRecords dataset. The goal is to uncover high-frequency issues, regional problem areas, and opportunities for optimization.

1. Descriptive Statistics

- Total number of maintenance events
- Counts of unique vehicles, parts, states, and event types
- Summary statistics for numeric fields (e.g., cost, mileage, event count)
- Date range and frequency of recorded maintenance events

2. Part Failure & Maintenance Frequency

- Identified the Top 10 most frequently serviced parts, revealing which components fail most often.
- Calculated event distributions by event_type (e.g., repair, replacement, inspection).
- Analyzed correlations between part failures and mileage (if available).

3. Geographic Insights

- Aggregated maintenance events by state to determine which regions experience the highest maintenance volume.
- Generated a state-by-part heatmap to identify geographic clusters of recurring failures.
- Highlighted states with potential environmental or usage-driven maintenance spikes.

4. Time-Series Analysis

- Resampled events monthly to visualize maintenance trends over time.
- Detected seasonal patterns or unusual spikes in service activity.
- Used rolling averages to smooth fluctuations and reveal long-term operational patterns.

5. Cost Analysis (if cost data provided)

- Calculated total, average, and state-level maintenance costs.
- Identified the most expensive parts to service and states with the highest repair costs.
- Highlighted parts that have high cost but low frequency, indicating potential inefficiencies.

6. State × Part Analysis

- Grouped records by state and part to find combinations with the highest event counts.
- Useful for predicting regional part stocking needs and preventing downtime.

7. Visual Insights (Python + Power BI)

- Bar charts for top failing parts and state event counts
- Line charts for monthly maintenance trends
- Map visuals for regional failure density
- Comparison charts for cost vs frequency

These insights help maintenance teams:

- Prioritize preventive maintenance
- Improve inventory planning

Reduce unexpected downtime

- Optimize fleet reliability and cost efficiency

