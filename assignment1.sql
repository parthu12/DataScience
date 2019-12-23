create database assignment1;
use  assignment1;
create table section(
course_id int unique ,
sec_id int unique,
semester int unique,
year int unique,
building varchar(20) unique,
room_no int unique,
time_slot_id int,
constraint
foreign key(course_id) references takes(course_id),
constraint
foreign key(sec_id) references takes(sec_id),
constraint
foreign key(semester) references takes(semester),
constraint
foreign key(year) references takes(year),
constraint
foreign key(course_id) references teaches(course_id),
constraint
foreign key(sec_id) references teaches(sec_id),
constraint
foreign key(semester) references teaches(semester),
constraint
foreign key(year) references teaches(year),
constraint 
foreign key(time_slot_id) references time_slot(time_slot_id)
);

create table classroom(
building varchar(20),
room_no int,
capacity int,
constraint
foreign key(building) references section(building),
constraint
foreign key(room_no) references section(room_no)
);
create table teaches(
ID int primary key,
course_id int unique,
sec_id int unique,
semester int unique,
year int unique
);
create table takes(
ID int primary key,
course_id int unique ,
sec_id int unique,
semester int unique,
year int unique,
grade char
);
create table time_slot(
time_slot_id int primary key,
day varchar(10),
start_time int,
end_time int);


create table prereq(
course_id int primary key,
prereq_id int unique);

create table course(
course_id int primary key,
title varchar(20),
dept_name varchar(25) unique,
credits int,
constraint
foreign key(course_id) references section(course_id),
constraint
foreign key(course_id) references prereq(course_id)
);

create table advisor(
s_id int ,
i_id int unique,
primary key (s_id,i_id)
);
drop table instructor;
describe advisor;



create table instructor(
ID int ,
name varchar(10),
dept_name varchar(25) unique,
salary int,
constraint
foreign key(ID) references advisor(i_id)
);

create table student(
ID int ,
name varchar(20),
dept_name varchar(25) unique,
tot_cred int,
constraint
foreign key(ID) references advisor(s_id),
constraint 
foreign key(ID) references takes(ID)
);

create table department(
dept_name varchar(25),
bulidibg varchar(20),
budget int,
constraint 
foreign key(dept_name) references student(dept_name),
constraint
foreign key(dept_name) references instructor(dept_name), 
constraint
foreign key(dept_name) references course(dept_name)); 