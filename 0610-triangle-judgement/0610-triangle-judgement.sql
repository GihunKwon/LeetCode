# Write your MySQL query statement below
SELECT *,
    CASE
        WHEN x+y <= z OR y+z <= x OR x+z <= y THEN 'No'
        WHEN x+y > z OR y+z > x OR x+z > y THEN 'Yes'
        END AS triangle
FROM Triangle