# Write your MySQL query statement below
(select name as results
from Users A
join MovieRating B ON A.user_id = B.user_id
group by name
order by COUNT(*) DESC, name
limit 1)

UNION ALL

(select title as results
from Movies A
join MovieRating B ON A.movie_id = B.movie_id
where created_at LIKE '2020-02%'
group by title
order by AVG(rating) DESC, title
limit 1)