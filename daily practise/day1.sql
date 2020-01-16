create database db_test;

use db_test;
create table student(
roll_no int primary key,
name varchar(20),
address varchar(100),
age int(3)
);
 drop table student;
 alter table student
 add hometown varchar(100);
 describe student;
 
 create table address(
 address_id int primary key,
 pin int(5),
 address varchar(200)
 );
 
 create table student1(
roll_no int,
name varchar(20),
address varchar(100),
age int(3)
);

create table student_address_mapping(
id int primary key,
student_id int,
address_id int,
constraint
 foreign key(student_id) references student(roll_no),
 constraint
 foreign key(address_id) references address(address_id)
);