# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers A
LEFT JOIN Orders B ON A.id = B.customerId
WHERE customerId IS NULL