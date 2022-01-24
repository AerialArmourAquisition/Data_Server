CREATE DATABASE data;
USE data;

CREATE TABLE labels (
    label_id INT NOT NULL AUTO_INCREMENT,
    label_path VARCHAR(255),
    PRIMARY KEY (label_id));

CREATE TABLE images(
    image_id INT NOT NULL AUTO_INCREMENT,
    image_path VARCHAR(255),
    PRIMARY KEY (image_id));