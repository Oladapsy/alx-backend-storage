-- a SQL script that creates a table users
-- CREATE DATABASE IF NOT EXISTS holberton1;
-- USE holberton1;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY (id)
);
