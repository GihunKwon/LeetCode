# Write your MySQL query statement below
DELETE A
FROM Person A, Person B
WHERE A.email = B.email AND A.id > B.id