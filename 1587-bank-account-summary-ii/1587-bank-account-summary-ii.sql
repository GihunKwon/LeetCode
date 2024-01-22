# Write your MySQL query statement below
SELECT A.name,SUM(B.amount) AS balance
FROM Users A
LEFT JOIN Transactions B ON A.account = B.account
GROUP BY A.name
HAVING balance > 10000