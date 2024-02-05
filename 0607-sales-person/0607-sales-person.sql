# Write your MySQL query statement below
SELECT A.name
FROM SalesPerson A
WHERE A.sales_id NOT IN (
    SELECT C.sales_id
    FROM Orders C
    JOIN Company B ON C.com_id = B.com_id
    WHERE B.name = 'RED'
)