[fleet_maintenance_schema.sql](https://github.com/user-attachments/files/23528910/fleet_maintenance_schema.sql)[fleet_maintenance_schema.sql](https://github.com/user-attachments/files/23528854/fleet_maintenance_schema.sql)[fleet_maintenance_schema.sql](https://github.com/user-attachments/files/23528833/fleet_maintenance_schema.sql)# Fleet Maintenance Analysis

### Overview

Analyzed fleet maintenance records using MySQL to identify part failure trends, regional performance issues, and cost drivers. Performed data cleaning, JOIN operations, and aggregations, then visualized insights in Excel/Power BI to support predictive maintenance decisions.

### Data Sources:

CSV dataset of fleet maintenance logs including part IDs, service timestamps, mileage, and regional repair data.

### Tools:

- MySQL — Imported and queried the fleet maintenance dataset [Download Here][Uploading fleet_maintenance_schema.sql…]()


- Python (Pandas, NumPy) — Data cleaning, transformation, and trend analysis
- Excel — Initial data inspection and verification [Download Here](https://github.com/user-attachments/files/23528645/FleetMaintenanceRecords.xlsx)

- Power BI — Visualized part failures, regional trends, and maintenance patterns
- Jupyter Notebook — Environment for exploratory and statistical analysis



## Highlights:
•	Imported and cleaned data using MySQL
•	Identified cost and failure trends by region
•	Built KPI dashboards in Power BI


## Structure:
/fleet-maintenance-data-analysis
 ├── /data              → FleetMaintenanceRecords.csv
 ├── /sql               → fleet_analysis_queries.sql
 └── /reports           → powerbi_dashboard
