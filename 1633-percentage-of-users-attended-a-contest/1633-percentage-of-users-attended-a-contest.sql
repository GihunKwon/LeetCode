# Write your MySQL query statement below
SELECT B.contest_id, ROUND((COUNT(B.user_id) / (SELECT COUNT(A.user_id) FROM Users A) ) * 100,2) AS percentage
FROM Register B
GROUP BY B.contest_id
ORDER BY percentage DESC, B.contest_id