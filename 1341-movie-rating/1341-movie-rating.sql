# Write your MySQL query statement below
(select B.name AS results
from MovieRating C
join Users B ON C.user_id = B.user_id
group by B.name
order by COUNT(*) DESC,B.name
limit 1)

UNION ALL

(select A.title AS results
from MovieRating C
join Movies A ON C.movie_id = A.movie_id
where C.created_at LIKE '2020-02%'
group by A.title
order by AVG(rating) DESC,A.title
limit 1)