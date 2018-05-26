SELECT Name as Employee
  FROM Employee as E
   INNER JOIN (SELECT Id, Salary FROM Employee) as F
   ON E.ManagerId = F.Id
  WHERE E.Salary > F.Salary
