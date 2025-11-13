[fleet_maintenance_schema.sql](https://github.com/user-attachments/files/23528854/fleet_maintenance_schema.sql)[fleet_maintenance_schema.sql](https://github.com/user-attachments/files/23528833/fleet_maintenance_schema.sql)# Fleet Maintenance Analysis

### Overview

Analyzed fleet maintenance records using MySQL to identify part failure trends, regional performance issues, and cost drivers. Performed data cleaning, JOIN operations, and aggregations, then visualized insights in Excel/Power BI to support predictive maintenance decisions.

### Data Sources:

CSV dataset of fleet maintenance logs including part IDs, service timestamps, mileage, and regional repair data.

### Tools:

- MySQL — Imported and queried the fleet maintenance dataset [Download Here][Uploa-- Create database (optional)
CREATE DATABASE IF NOT EXISTS fleet_maintenance;
USE fleet_maintenance;

-- Create PartsMaintenance table
CREATE TABLE PartsMaintenance (
    vehicle_id   BIGINT,
    state        CHAR(2),
    repair       VARCHAR(100),
    reason       VARCHAR(100),
    year         YEAR,
    make         VARCHAR(50),
    body_type    VARCHAR(100)
);

-- Load data from FleetMaintenanceRecords.csv
-- Update the path to where the CSV lives on your machine/server
LOAD DATA INFILE '/path/to/FleetMaintenanceRecords.csv'
INTO TABLE PartsMaintenance
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    vehicle_id,
    state,
    repair,
    reason,
    year,
    make,
    body_type
);
ding fleet_maintenance_schema.sql…]()

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
