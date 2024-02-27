# Write your MySQL query statement below
SELECT B.name
FROM Employee A
JOIN Employee B ON B.id = A.managerId
GROUP BY A.managerId
HAVING COUNT(A.managerId) >= 5