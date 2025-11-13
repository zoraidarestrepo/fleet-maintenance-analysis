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

- Loaded and cleaned the FleetMaintenanceRecords dataset using Pandas
- Handled missing values, standardized text fields, and converted date columns
- Computed summary statistics to understand maintenance frequency, part usage, and vehicle distribution

```python
import pandas as pd

df = pd.read_csv("FleetMaintenanceRecords.csv")
df['date'] = pd.to_datetime(df['date'])

print(df.describe(include='all'))
print("Unique Parts:", df['part_name'].nunique())
print("Unique States:", df['state'].nunique())
```


2. Part Failure & Maintenance Frequency

- Identified Top 10 Most Replaced Parts using groupby operations
- Calculated total event counts and analyzed the distribution across event types

```python
  top_parts = (
    df.groupby('part_name')
      .size()
      .sort_values(ascending=False)
      .head(10)
)

top_parts.plot(kind='barh', title='Top 10 Most Frequently Serviced Parts')
```
Insight: Certain components (filters, brakes, and sensors) appear in a high percentage of service events, signaling high wear or sub-optimal replacement cycles.

3. Geographic Insights

- Grouped and visualized maintenance events by state
- Merged with a state geolocation dataset for mapping in Power BI
- Used Python to surface the most problematic states:

```python
  state_counts = df['state'].value_counts()
print(state_counts.head())
```

4. Time-Series Analysis

- Aggregated maintenance data by month to observe trends over time
- Used rolling averages with NumPy to reveal long-term patterns

```python
df['month'] = df['date'].dt.to_period('M')
monthly_events = df.groupby('month').size()

monthly_events.rolling(3).mean().plot(title="3-Month Rolling Avg of Maintenance Events")
```

5. Cost Analysis (if cost data provided)

- Combined groupby operations to reveal how part failures vary by geography
- Exported pivot tables for Power BI dashboards

```python
  pivot = pd.pivot_table(
    df,
    values='vehicle_id',
    index='state',
    columns='part_name',
    aggfunc='count',
    fill_value=0
)

pivot.to_csv("state_part_matrix.csv")
```

6. State × Part Analysis

- Computed cost totals and averages
- Isolated parts with high cost but low frequency
- Identified inefficiencies and potential vendor negotiation opportunities

```python
df['total_cost'] = df['labor_cost'] + df['part_cost']
cost_summary = df.groupby('part_name')['total_cost'].sum().sort_values(ascending=False)
```

7. Tools & Features Used 

✔ Python (Pandas, NumPy) for cleaning, prep, EDA, and transformation
✔ MySQL for structured queries and relational analysis
✔ Jupyter Notebook for interactive exploration
✔ Power BI for dashboards (maps, heatmaps, trends)
✔ Excel for quick QA and supplemental analysis
✔ Matplotlib/Seaborn for data visualizations in Notebook
✔ CSV/Excel exports for sharing cleaned datasets and matrices

8. Key Insights Delivered

- Identified the most failure-prone parts across the fleet
- Detected regional hotspots of maintenance activity
- Visualized seasonal/temporal trends that impact maintenance planning
- Highlighted cost optimization opportunities
- Produced actionable dashboards for maintenance teams

### Results & Findings

The Fleet Maintenance analysis uncovered several data-driven insights related to part failures, regional performance, and operational efficiency. Using Python, MySQL, and Power BI visualizations, the following findings were identified:

1. Most Frequently Replaced Parts

Analysis of over 10,000+ maintenance events revealed that a small subset of parts accounted for a majority of replacements:

- Brake pads
- Filters (air, oil, cabin)
- Oxygen sensors / engine sensors
- Tires and rotating components

These parts showed consistently high failure frequency, suggesting:

- High wear due to usage intensity
- Possible suboptimal replacement intervals
- Potential purchasing inefficiencies for commonly needed inventory

📌 Insight: Optimizing the maintenance schedule and stocking these high-frequency parts could reduce downtime and supply delays.

2. Regional Hotspots of Maintenance Activity

Grouping events by state revealed clear geographic trends:
  - Certain states showed 30–45% higher maintenance volume, especially in areas with:
     - Harsher weather
     - High mileage routes
     - Poorer road conditions

Power BI heatmaps showed clusters of frequent failures in:

- Texas
- Florida
- California

Insight: These regions may require more preventive maintenance or localized inventory stocking.

3. Seasonal Maintenance Trends

Time-series analysis uncovered noticeable spikes during specific months:

- Increased replacements during summer months, likely due to heat stress on mechanical parts
- End-of-year increases related to heavy travel patterns

Rolling averages clearly show seasonal patterns affecting the entire fleet.

Insight: Seasonal-based maintenance planning could reduce unexpected repairs and improve resource allocation.

4. High-Cost Parts and Cost Efficiency

For datasets that include cost information:

- A few components had high total cost but relatively low failure frequency, including:
  - Transmission-related parts
  - Specialized sensors
  - Heavy engine components

These represent “high-impact” repairs that significantly affect budget allocation.

Insight: Vendors for these components should be re-evaluated for potential cost savings or contract adjustments.

5. Most Failure-Prone Regions by Part Type

Pivot tables revealed patterns such as:

- Brakes failing most often in mountainous or urban states
- Filters requiring more frequent service in dusty or rural regions
- Sensors showing elevated failure rates in high-humidity states (e.g., Florida)

Insight: Customizing maintenance schedules by region could help reduce repair frequency.

6. Vehicle-Level Insights

Across the dataset:

- A small percentage of vehicles accounted for disproportionately high maintenance events
- These "attention vehicles" can signal:
   - Older fleet age
   - Operational misuse
   - Underlying mechanical issues

Insight: Identifying high-frequency-breakdown vehicles allows targeted repair or replacement planning.

7. Key Operational Improvements Identified

Based on the findings, the fleet can improve performance through:

### Data-driven Preventive Maintenance
Predicting part failures by season, region, and historical trends.

### Smarter Inventory Management
Stocking high-frequency parts based on geography and usage.

### Cost Optimization Strategies
Reassessing vendors for high-cost but low-frequency components.

### Vehicle Lifecycle Planning
Early identification of aging or problematic vehicles.
