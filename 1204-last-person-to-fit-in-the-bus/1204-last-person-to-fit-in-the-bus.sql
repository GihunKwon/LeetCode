# Write your MySQL query statement below
WITH total_weight AS (
    SELECT person_name,turn,SUM(weight) OVER (ORDER BY turn) AS W
    from Queue
)

SELECT person_name
FROM total_weight
WHERE w <= 1000
ORDER BY turn DESC
LIMIT 1