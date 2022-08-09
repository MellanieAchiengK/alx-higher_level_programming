-- Displays max temperature
SELECT state, MAX(value) AS max_temp FROM temperatures ORDER BY state;
