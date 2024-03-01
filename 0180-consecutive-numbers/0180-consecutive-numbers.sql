# Write your MySQL query statement below
SELECT DISTINCT A.num as ConsecutiveNums
FROM logs A, logs B, logs C
WHERE
    A.id = B.id + 1 AND
    B.id = C.id + 1 AND
    A.num = B.num AND
    B.num = C.num