# Write your MySQL query statement below
SELECT id, 
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE NULL END) AS Jan_REVENUE,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE NULL END) AS Feb_REVENUE,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE NULL END) AS Mar_REVENUE,
    SUM(CASE WHEN month = 'Apr' THEN revenue ELSE NULL END) AS Apr_REVENUE,
    SUM(CASE WHEN month = 'May' THEN revenue ELSE NULL END) AS May_REVENUE,
    SUM(CASE WHEN month = 'Jun' THEN revenue ELSE NULL END) AS Jun_REVENUE,
    SUM(CASE WHEN month = 'Jul' THEN revenue ELSE NULL END) AS Jul_REVENUE,
    SUM(CASE WHEN month = 'Aug' THEN revenue ELSE NULL END) AS Aug_REVENUE,
    SUM(CASE WHEN month = 'Sep' THEN revenue ELSE NULL END) AS Sep_REVENUE,
    SUM(CASE WHEN month = 'Oct' THEN revenue ELSE NULL END) AS Oct_REVENUE,
    SUM(CASE WHEN month = 'Nov' THEN revenue ELSE NULL END) AS Nov_REVENUE,
    SUM(CASE WHEN month = 'Dec' THEN revenue ELSE NULL END) AS Dec_REVENUE
FROM Department
GROUP BY id