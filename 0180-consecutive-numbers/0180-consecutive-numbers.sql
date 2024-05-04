# Write your MySQL query statement below
SELECT DISTINCT A.NUM AS ConsecutiveNums
FROM Logs A, Logs B, Logs c
WHERE A.id = B.id + 1 AND
    B.id = C.id + 1 AND
    A.num = B.num AND
    B.num = C.num