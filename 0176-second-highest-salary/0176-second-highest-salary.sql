# Write your MySQL query statement below
# SELECT 
# (select DISTINCT salary
# FROM Employee
# ORDER BY salary DESC
# LIMIT 1,1)
# as SecondHighestSalary

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (select MAX(salary) from Employee)