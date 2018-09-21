# Write your MySQL query statement below
SELECT Person.Email
FROM Person
GROUP BY Person.Email
HAVING COUNT(Person.Email) > 1
