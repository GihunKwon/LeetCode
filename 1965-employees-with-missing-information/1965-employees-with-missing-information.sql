# Write your MySQL query statement below
SELECT A.employee_id
FROM Employees A
LEFT JOIN Salaries B ON A.employee_id = B.employee_id
WHERE B.salary IS NULL
UNION
SELECT B.employee_id
FROM Employees A
RIGHT JOIN Salaries B ON A.employee_id = B.employee_id
WHERE A.NAME IS NULL
ORDER BY employee_id