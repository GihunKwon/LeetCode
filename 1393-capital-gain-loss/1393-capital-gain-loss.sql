# Write your MySQL query statement below
SELECT stock_name,  SUM(CASE 
        WHEN operation = 'Sell' THEN price
        WHEN operation = 'Buy' Then -price
        END) AS capital_gain_loss
FROM Stocks
GROUP BY 1