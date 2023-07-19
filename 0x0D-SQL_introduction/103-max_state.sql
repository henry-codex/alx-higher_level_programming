-- Max temperature of each state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUp BY state ORDER BY state, max_temp DESC LIMIT 3;
