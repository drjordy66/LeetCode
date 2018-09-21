CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE X INT DEFAULT N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT(
          SELECT DISTINCT Employee.Salary
          FROM Employee
          ORDER BY Employee.Salary DESC
          LIMIT 1
          OFFSET X
      ) AS getNthHighestSalary
  );
END
