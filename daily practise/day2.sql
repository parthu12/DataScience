use employees;

insert into db_test.address(address_id,pin,address) values(2,201,'hyd');
 show tables;
 select * from address;
select distinct(dept_no) from departments;
 select * from employees.salaries;
 select max(salary) from employees.salaries;
 select count(*) from employees.salaries;
 
 
Select count(distinct(emp_no)) from employees.salaries;

select avg(salary) from employees.salaries;

select sum(salary) from employees.salaries;

select * from employees.employees;
select first_name from employees.employees where first_name like 'A%';
select first_name from employees.employees where first_name like '_A%';