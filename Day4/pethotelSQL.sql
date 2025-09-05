-- CREATE DATABASE pet_hotel

USE pet_hotel;
-- CREATE TABLE Guardian(
-- 	guardian_id int primary key auto_increment,
--     name varchar(15) not null,
--     phone_number varchar(15) not null,
--     address varchar (300)
-- );

-- CREATE TABLE PET(
-- 	pet_id int primary key auto_increment,
--     guardian_id int,
--     foreign key (guardian_id) REFERENCES Guardian (guardian_id),
--     name varchar(15),
--     is_neutered enum('예', '아니오') Not null,
--     breed varchar(15), 
--     size_type enum('소형견', '중대형견') not null,
--     allergy_info text
-- );

-- CREATE TABLE service_plan(
-- plan_id int primary key auto_increment,
-- plan_name varchar(10) not null unique, 
-- base_price int not null
-- );

-- CREATE TABLE reservation(
-- reservation_id int primary key auto_increment,
-- pet_id int not null,
-- foreign key (pet_id) references PET (pet_id),
-- plan_id int not null,
-- foreign key (plan_id) references service_plan (plan_id),
-- check_in_datetime datetime not null,
-- check_out_datetime datetime not null,
-- meal_type enum('호텔제공식', '특수식') not null,
-- snack_type enum('호텔제공식', '특수식') not null, 
-- walk_option boolean not null, 
-- final_price int not null
-- );