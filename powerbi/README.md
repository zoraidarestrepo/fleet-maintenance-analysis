## Power BI Report

A Power BI report was built on top of the FleetMaintenanceRecords dataset to provide interactive, business-friendly insights.

### Data Source
- **Dataset:** FleetMaintenanceRecords (CSV/Excel)
- **Loaded into Power BI** using Power Query
- Basic cleaning applied (data types, date parsing, trimming text fields).

### Report Pages

#### 1. Overview Dashboard
- **Cards**:
  - Total number of maintenance events
  - Number of unique parts
  - Number of states covered
- **Line chart**:
  - Maintenance events over time (by month)
- **Clustered column chart**:
  - Events by state

#### 2. Parts Analysis
- **Bar chart**:
  - Top 10 most frequently serviced parts
- **Stacked bar chart**:
  - Event count by part and event type
- **Slicer filters**:
  - State
  - Date range
  - Event type

#### 3. State & Regional Insights
- **Map visual or filled map**:
  - Maintenance events by state
- **Bar chart**:
  - Total events and/or total cost by state
- **Table visual**:
  - State, part name, event count, and (optional) total cost

#### 4. Cost Analysis (if cost is available)
- **Bar chart**:
  - Total maintenance cost by part
- **Column chart**:
  - Total cost by state
- **Card**:
  - Average cost per event

### Example Measures (DAX)

```DAX
Total Events = COUNTROWS(FleetMaintenanceRecords)

Total Cost = SUM(FleetMaintenanceRecords[cost])

Average Cost per Event = 
DIVIDE(
    [Total Cost],
    [Total Events],
    0
)

##This report allows operations and maintenance teams to:

- Quickly see which parts are failing most often

- Identify high-risk states or regions

- Track trends in maintenance volume over time

- Focus on cost drivers and opportunities for preventive maintenance
