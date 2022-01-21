CREATE DATABASE data;
USE data;

CREATE TABLE labels (
    label_id INT NOT NULL AUTO_INCREMENT,
    label_file BLOB,
    PRIMARY KEY (label_id));

CREATE TABLE images(
    image_id INT NOT NULL AUTO_INCREMENT,
    image BLOB,
    PRIMARY KEY (image_id));