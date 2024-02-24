# Write your MySQL query statement below
SELECT A.user_id AS buyer_id,A.join_date,COUNT(B.order_id) AS orders_in_2019
FROM Users A
LEFT JOIN Orders B ON B.buyer_id = A.user_id AND YEAR(order_date) = '2019'
GROUP BY A.user_id