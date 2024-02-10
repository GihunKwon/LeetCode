# Write your MySQL query statement below
SELECT A.name, IFNULL( SUM(B.distance) , 0 ) AS travelled_distance
FROM Users A
LEFT JOIN Rides B ON A.id = B.user_id
GROUP BY A.id
ORDER BY travelled_distance DESC, A.name