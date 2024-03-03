# Write your MySQL query statement below
SELECT 
(select DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1,1)
as SecondHighestSalary

