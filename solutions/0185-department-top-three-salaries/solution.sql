# Write your MySQL query statement below
select d.name as Department ,e.name as Employee , e.salary as Salary  
from Employee e,Department d
where d.id=e.departmentId 
and  3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
      AND e2.salary > e.salary
)


order by e.salary desc
