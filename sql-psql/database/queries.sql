--- SELECT QUERY
SELECT * FROM Users;

INSERT INTO Users (id,name,email,password) VALUES (
    101, 'Hari', 'hari@ex.com', 'fa;sdlfjas'),
    (102, 'Ram', 'ram@ex.com', 'a;sldfj;ajs'),
    (103, 'Anish', 'anish@ex.com', 'f;alsdfla'),
    (104, 'false', 'false@ex.com', 'fasdfa'
);

INSERT INTO Notes (user_id, title, content) VALUES (
    101, 'Note 1', 'Content 1'
);

INSERT INTO Notes (user_id, title, content) VALUES (
    102, 'Note 2', 'Content 2'
);

INSERT INTO Notes (user_id, title, content) VALUES (
    103, 'Note 3', 'Content 3'
);

INSERT INTO Notes (user_id, title, content) VALUES (
    104, 'Note 4', 'Content 4'
);


SELECT * FROM Notes ORDER BY title ASC;

SELECT * FROM Users ORDER BY name ASC LIMIT 3;

UPDATE Users SET name = 'Haea' WHERE id = 104;

SELECT name FROM Users JOIN Notes ON Users.id = Notes.user_id WHERE Notes.title = 'Note 3';
