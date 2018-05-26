/* Write your T-SQL query statement below */

select 
  Department,
  Employee,
  Salary
from(
    select
      t.Department as Department,
      t.Name as Employee,
      t.Salary as Salary,
      dense_rank() over (partition by t.Department
                        order by t.Salary desc) as row_number  
    from(
        select 
           d.Name as Department,
           e.Name as Name,
           e.Salary as Salary
         from 
           Employee as e
         inner join Department as d
         on e.DepartmentId = d.Id
    )t
)t1
where t1.row_number = 1
