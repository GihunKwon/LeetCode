# Write your MySQL query statement below
SELECT A.product_name,SUM(B.unit) AS unit
FROM Products A
LEFT JOIN Orders B ON A.product_id = B.product_id
WHERE B.order_date LIKE '2020-02%'
GROUP BY 1
HAVING unit >= 100