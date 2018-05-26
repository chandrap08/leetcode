CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select MAX(Salary)
        FROM Employee as Emp1
           WHERE (N-1) = (
             SELECT COUNT(DISTINCT(Salary)) FROM Employee as Emp2
               WHERE Emp2.Salary > Emp1.Salary
           )
  );
END