# Write your MySQL query statement below
WITH NUM_ID AS (
    select requester_id AS id
    from RequestAccepted
    UNION ALL
    select accepter_id AS id
    from RequestAccepted
)

SELECT id,COUNT(id) AS num
FROM NUM_ID
GROUP BY id
ORDER BY num DESC
LIMIT 1