# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (select requester_id as id
        from RequestAccepted
        UNION ALL
        select accepter_id as id
        from RequestAccepted) AS A
GROUP BY id
ORDER BY num DESC
LIMIT 1