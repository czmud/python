-- create 3 new users
INSERT INTO users (first_name, last_name, email) VALUES
('john', 'sampson', 'jsampson@gmail.com'),
('ellery', 'quinn', 'equinn@gmail.com'),
('sahil', 'patel', 'spatel@gmail.com');

-- retrieve all users
SELECT * FROM users;

-- retrieve the first user by email address
SELECT * FROM users
WHERE users.email = 'jsampson@gmail.com';

-- retrive the last user by id
SELECT * FROM users
WHERE users.id = 3;

-- change user id = 3 to have last name pancakes
UPDATE users SET last_name = 'pancakes' 
WHERE id = 3;

-- delete user id = 2 from database
DELETE FROM users WHERE id = 2;

-- get all users sorted by first name
SELECT * FROM users
ORDER BY users.first_name;

-- get all users sorted by first name in descending order
SELECT * FROM users
ORDER BY users.first_name DESC;