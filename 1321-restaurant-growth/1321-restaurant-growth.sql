# Write your MySQL query statement below
SELECT visited_on,
    (select SUM(amount)
    from Customer
    where visited_on BETWEEN DATE_SUB(A.visited_on,INTERVAL 6 DAY) AND A.visited_on) AS amount,
    ROUND(
        (select SUM(amount) / 7
        from Customer
        where visited_on BETWEEN DATE_SUB(A.visited_on,INTERVAL 6 DAY) AND A.visited_on),2) AS average_amount
FROM Customer A
WHERE visited_on >= (
    select DATE_ADD(MIN(visited_on),INTERVAL 6 DAY)
    from Customer
)
GROUP BY visited_on