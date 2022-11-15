/* Write your PL/SQL query statement below */

with help_table as 
(
   select d.id, e.salary from employee e join department d on d.id = e.departmentid 
    group by d.id, e.salary
    order by d.id asc
)
select department.name as department, employee.name as employee, t.salary from (select id, salary from (select id, salary, row_number() over(partition by id order by salary desc) as nums from help_table) where nums <= 3) t join employee on employee.departmentid = t.id join department on employee.departmentid = department.id where employee.salary = t.salary;