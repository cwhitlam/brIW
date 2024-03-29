CREATE DATABASE IF NOT EXISTS chris;

USE chris;

CREATE TABLE chris.tbl_drinks (
    drink_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE chris.tbl_people (
    person_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    preferred_drink_id INTEGER
);

CREATE TABLE chris.tbl_rounds (
    round_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    maker_id INTEGER NOT NULL,
    created_datetime DATETIME NOT NULL,
    expiry_datetime DATETIME NOT NULL,
    FOREIGN KEY (maker_id) REFERENCES tbl_people(person_id)
);

CREATE TABLE chris.tbl_orders (
    order_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    round_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    drink_id INTEGER NOT NULL,
    special_requests VARCHAR(100),
    FOREIGN KEY (round_id) REFERENCES tbl_rounds(round_id),
    FOREIGN KEY (person_id) REFERENCES tbl_people(person_id),
    FOREIGN KEY (drink_id) REFERENCES tbl_drinks(drink_id)
);


ALTER TABLE tbl_orders ADD special_requests VARCHAR(100);  