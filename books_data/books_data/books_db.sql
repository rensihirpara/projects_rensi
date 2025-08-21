CREATE DATABASE IF NOT EXISTS books_db;

USE books_db;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price VARCHAR(20),
    availability VARCHAR(50),
    rating VARCHAR(20)
);
