# Write your MySQL query statement below
SELECT person_name
FROM (
    select person_name,turn,sum(weight) over (order by turn) as cum
    from Queue) A
WHERE cum <= 1000
ORDER BY turn DESC
LIMIT 1 