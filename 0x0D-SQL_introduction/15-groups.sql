-- lists number of records with same score of each score value(ie each score col)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
