# Write your MySQL query statement below
SELECT A.name, IF (SUM(B.distance), SUM(B.distance), 0) AS travelled_distance
FROM Users A
lEFT JOIN Rides B ON A.id = B.user_id
GROUP BY A.id
ORDER BY travelled_distance DESC , A.name ASC