# Write your MySQL query statement below
SELECT B.name as Department, A.name as Employee, A.salary as Salary
FROM Employee A
JOIN Department B ON A.departmentId = B.id
WHERE (A.departmentId,A.salary) IN
    (
    select departmentId,MAX(salary)
    from Employee
    group by departmentId
    )