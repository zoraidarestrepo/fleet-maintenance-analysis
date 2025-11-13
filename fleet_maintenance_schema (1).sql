-- Create database (optional)
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
