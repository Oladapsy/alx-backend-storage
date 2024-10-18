-- a SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email CHAR(255) NOT_NULL UNIQUE,
    name CHAR(255);
    PRIMARY KEY (id)
);
