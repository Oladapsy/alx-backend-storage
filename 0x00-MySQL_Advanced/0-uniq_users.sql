-- a SQL script that creates a table users

CREATE TABLE users IF NOT EXISTS (
	id INT NOT_NULL AUTO_INCREMENT PRIMARY KEY,
	email CHAR(255) NOT_NULL UNIQUE,
       	name CHAR(255),
);
