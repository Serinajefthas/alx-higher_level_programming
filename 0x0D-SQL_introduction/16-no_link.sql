-- lists all records of 'second_table'
-- don't list rows without 'name' value
-- display score then name (in this order)
-- records in desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
