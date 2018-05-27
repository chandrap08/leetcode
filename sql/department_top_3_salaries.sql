# Write your MySQL query statement below

SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
 FROM Employee e INNER JOIN Department d ON d.Id = e.DepartmentId
 WHERE (SELECT COUNT(DISTINCT Salary) FROM Employee e1
       WHERE e1.DepartmentId = e.DepartmentId AND e1.Salary > e.Salary) < 3
 ORDER BY e.DepartmentId, e.Salary DESC