-- 1. Total records
SELECT COUNT(*) AS total_events
FROM FleetMaintenanceRecords;

-- 2. Top 10 most frequently replaced/serviced parts
SELECT 
    part_name,
    COUNT(*) AS event_count
FROM FleetMaintenanceRecords
GROUP BY part_name
ORDER BY event_count DESC
LIMIT 10;

-- 3. Events per state
SELECT 
    state,
    COUNT(*) AS event_count
FROM FleetMaintenanceRecords
GROUP BY state
ORDER BY event_count DESC;

-- 4. Event type distribution
SELECT 
    event_type,
    COUNT(*) AS event_count
FROM FleetMaintenanceRecords
GROUP BY event_type
ORDER BY event_count DESC;

-- 5. Events per month
SELECT 
    DATE_FORMAT(event_date, '%Y-%m-01') AS month,
    COUNT(*) AS event_count
FROM FleetMaintenanceRecords
GROUP BY month
ORDER BY month;

-- 6. State x part combination – top 20
SELECT 
    state,
    part_name,
    COUNT(*) AS event_count
FROM FleetMaintenanceRecords
GROUP BY state, part_name
ORDER BY event_count DESC
LIMIT 20;

-- 7. Cost analysis by state (if cost column exists)
SELECT 
    state,
    COUNT(*) AS event_count,
    SUM(cost) AS total_cost,
    AVG(cost) AS avg_cost
FROM FleetMaintenanceRecords
GROUP BY state
ORDER BY total_cost DESC;
