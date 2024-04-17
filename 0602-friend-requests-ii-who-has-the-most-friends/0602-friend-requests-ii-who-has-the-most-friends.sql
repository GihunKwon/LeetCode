# Write your MySQL query statement below
with cnt as (
select requester_id as id
from RequestAccepted
UNION ALL
select accepter_id as id
from RequestAccepted )

SELECT id, COUNT(id) as num
FROM cnt
GROUP BY id
ORDER BY num DESC
LIMIT 1