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




## Highlights:
•	Imported and cleaned data using MySQL
•	Identified cost and failure trends by region
•	Built KPI dashboards in Power BI


## Structure:
/fleet-maintenance-data-analysis
 ├── /data              → FleetMaintenanceRecords.csv
 ├── /sql               → fleet_analysis_queries.sql
 └── /reports           → powerbi_dashboard
