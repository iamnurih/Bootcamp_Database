-- CREATE DATABASE practiceschema

USE practiceschema;

-- CREATE TABLE user(
-- id int auto_increment primary key,
-- password varchar(4),
-- name varchar(3), 
-- gender enum('male', 'female'),
-- email varchar(15),
-- birthday char(6),
-- age TINYINT, 
-- company enum('samsung', 'lg', 'hyundai')
-- );


create table boards(
id int primary key auto_increment,
title varchar(5),
content varchar(10),
likes INT CHECK (likes between 1 and 100),
img char(1) default 'c',
user_id int, 
foreign key(user_id) references user(id)
);