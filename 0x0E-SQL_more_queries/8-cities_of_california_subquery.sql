-- Lists all cities of California found in DB 
-- only where name is California and results in asc order
SELECT id, state_id
FROM hbtn_0d_usa
WHERE name = 'California'
ORDER BY cities.id
