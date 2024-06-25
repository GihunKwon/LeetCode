# Write your MySQL query statement below
(SELECT B.name AS results
FROM MovieRating C
JOIN Users B ON C.user_id = B.user_id
GROUP BY B.name
ORDER BY COUNT(*) DESC, B.name
LIMIT 1)
UNION ALL
(SELECT A.title AS results
FROM MovieRating C
JOIN Movies A ON C.movie_id = A.movie_id
WHERE YEAR(C.created_at) = '2020'
        AND MONTH(C.created_at) = '02'
GROUP BY C.movie_id
ORDER BY AVG(C.rating) DESC, A.title
LIMIT 1)