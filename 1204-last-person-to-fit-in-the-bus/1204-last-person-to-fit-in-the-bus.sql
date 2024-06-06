# Write your MySQL query statement below
WITH total AS (
    select person_name,turn,SUM(weight) OVER (ORDER BY turn) AS sum_weight
    from Queue
)

SELECT person_name
FROM total
WHERE sum_weight <= 1000
ORDER BY turn DESC
LIMIT 1