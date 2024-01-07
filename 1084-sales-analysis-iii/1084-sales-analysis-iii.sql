# Write your MySQL query statement below
SELECT A.product_id,A.product_name
FROM Product A
JOIN Sales B ON A.product_id = B.product_id
GROUP BY product_id
Having MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'