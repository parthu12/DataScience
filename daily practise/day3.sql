select * from employees.employees where gender ="M" and first_name like 'P%';
SELECT * FROM employees.employees order by hire_date desc ;
SELECT * FROM employees.dept_manager WHERE dept_no IN ('d009','d005');


select e.first_name AS name,d.dept_name AS department from
 employees e
     join 
    dept_emp de 
    on 
    de.emp_no = e.emp_no
    join 
    departments d
    on de.dept_no = d.dept_no
    ;

