# Write your MySQL query statement below
SELECT A.employee_id
FROM Employees A
LEFT JOIN Salaries B
ON A.employee_id = B.employee_id
WHERE B.salary IS NULL

UNION

SELECT B.employee_id
FROM Salaries B
LEFT JOIN Employees A
ON A.employee_id = B.employee_id
WHERE A.name IS NULL
ORDER BY 1