# Write your MySQL query statement below
DELETE FROM Person
WHERE Person.Id NOT IN (
    SELECT a.Id
    FROM (
        SELECT MIN(Person.Id) AS Id
        FROM Person
        GROUP BY Person.Email
    ) AS a
)
