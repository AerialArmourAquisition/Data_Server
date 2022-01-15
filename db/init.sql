CREATE DATABASE data;
USE data;

CREATE TABLE labels (
    label_id INT NOT NULL AUTO_INCREMENT,
    label_file VARCHAR(255) NOT NULL,
    PRIMARY KEY (label_id));

CREATE TABLE images(
    image_id INT NOT NULL AUTO_INCREMENT,
    image VARCHAR(255) NOT NULL,
    PRIMARY KEY (image_id));