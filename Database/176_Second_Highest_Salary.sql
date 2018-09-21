# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT Employee.Salary
    FROM Employee
    ORDER BY Employee.Salary DESC
    LIMIT 1
    OFFSET 1
) AS SecondHighestSalary
