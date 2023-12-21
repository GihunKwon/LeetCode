# Write your MySQL query statement below
SELECT A.name
FROM SalesPerson A
WHERE A.sales_id not in (
    SELECT B.sales_id
    FROM Orders B
    JOIN Company C
    ON C.com_id = B.com_id
    WHERE c.name = 'RED'
)
