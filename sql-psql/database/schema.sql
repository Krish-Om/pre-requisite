CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
);


INSERT INTO Users (id,name,email,password) VALUES (
    101, 'Hari', 'hari@ex.com', 'fa;sdlfjas'),
    (102, 'Ram', 'ram@ex.com', 'a;sldfj;ajs'),
    (103, 'Anish', 'anish@ex.com', 'f;alsdfla'),
    (104, 'false', 'false@ex.com', 'fasdfa')
);
