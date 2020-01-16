select * from employees.employees where first_name like 's%'
union 
select * from employees.employees where first_name like 'p%';
select * from employees.salaries sal join employees.employees emp on emp.emp_no = sal.emp_no
where sal.salary between 60000 and 65000;

select * from employees.employees where first_name like 's%'

union

select * from employees.employees where first_name like 'a%';


select sal.salary AS salary, emp.first_name AS firstName,emp.last_name AS lastName from employees.salaries sal
 join 
 employees.employees emp
 on
 emp.emp_no = sal.emp_no
  where 
  sal.salary BETWEEN
  60000 AND 65000
 ;
select min(sal.salary),d.dept_name from employees.employees emp join employees.salaries sal 
on emp.emp_no = sal.emp_no join employees.dept_emp de on
emp.emp_no = de.emp_no
join employees.departments d on 
de.dept_no =d.dept_no
group by
d.dept_name
having d.dept_name like 's%';


select sal.salary,emp.first_name from employees.employees emp join employees.salaries sal 
on emp.emp_no = sal.emp_no
where
 EMP.emp_no NOT IN 
  (
     SELECT distinct(emp_no) FROM 
     employees.dept_emp WHERE dept_no='d002'
 ); 
 
 SELECT  EMP.first_name,SAL.salary FROM 
 employees.EMPLOYEES EMP
JOIN
 employees.SALARIES SAL
ON
 EMP.emp_no = SAL.emp_no
WHERE 
 EMP.emp_no NOT IN 
    (
     SELECT distinct(emp_no) FROM 
     employees.dept_emp WHERE dept_no='d002'
 );



update employees.employees set gender ='f' where emp_no = '10002'; 
