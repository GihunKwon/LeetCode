# Write your MySQL query statement below
SELECT A.machine_id, ROUND(AVG(B.timestamp - A.timestamp),3) AS processing_time
FROM Activity A
JOIN Activity B
ON A.process_id = B.process_id AND A.machine_id = B.machine_id AND A.timestamp < B.timestamp
GROUP BY A.machine_id