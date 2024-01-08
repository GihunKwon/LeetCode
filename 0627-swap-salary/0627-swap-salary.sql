# Write your MySQL query statement below
UPDATE Salary
SET sex =
    case when sex = 'm' THEN 'f'
    ELSE 'm'
END