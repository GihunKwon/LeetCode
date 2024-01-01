# Write your MySQL query statement below
SELECT B.contest_id,ROUND((COUNT(B.user_id)/ (SELECT COUNT(user_id) FROM Users) * 100) , 2) AS percentage
FROM Users A
RIGHT JOIN Register B
ON A.user_id = B.user_id
GROUP BY B.contest_id
ORDER BY percentage DESC, B.contest_id
