CREATE TABLE people (
    person_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL
);

CREATE TABLE drinks (
    drink_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE preferences (
    person_id INTEGER PRIMARY KEY,
    drink_id INTEGER NOT NULL,
    FOREIGN KEY (person_id) REFERENCES people(person_id),
    FOREIGN KEY (drink_id) REFERENCES drinks(drink_id)
);
