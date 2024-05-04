CREATE DATABASE local_db;
USE local_db;
CREATE TABLE products (
    products_id int not NULL,
    `name` varchar(255) NOT NULL DEFAULT '',
    price int(10) NOT NULL,
    quanity int(10) NOT NULL,
    image_url varchar(255) NOT NULL DEFAULT '',
    PRIMARY KEY (products_id)
);