# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM Insurance
WHERE (lat,lon) NOT IN (
    select lat,lon
    from Insurance
    group by lat,lon
    having COUNT(lat) > 1 AND COUNT(lon) > 1
)
AND (tiv_2015) IN (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having COUNT(tiv_2015) > 1
)