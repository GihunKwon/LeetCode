# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT player_id) / (select COUNT(DISTINCT player_id) from Activity),2) AS fraction
FROM Activity
WHERE (player_id,DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
    select player_id,min(event_date)
    from Activity
    group by player_id
)