-- create 5 users
INSERT INTO users (first_name, last_name) VALUES
('jane', 'amsden'),
('emily', 'dixon'),
('theodore', 'dostoevsky'),
('william', 'shapiro'),
('lao', 'xiu');

-- create 5 books
INSERT INTO books (title, num_of_pages) VALUES
('c sharp', 101),
('java', 250),
('python', 578),
('php', 589),
('ruby', 415);

-- change the c sharp book to C#
UPDATE books SET title = 'c#' WHERE id = 1;

-- change the first name of the 4th user to bill
UPDATE users SET first_name = 'bill' WHERE id = 4;

-- first user favorite first 2 books
INSERT INTO favorites (user_id, book_id) VALUE
(1,1),
(1,2);

-- second user favorite first 3 books
INSERT INTO favorites (user_id, book_id) VALUE
(2,1),
(2,2),
(2,3);

-- third user favorite first 4 books
INSERT INTO favorites (user_id, book_id) VALUE
(3,1),
(3,2),
(3,3),
(3,4);

-- fourth user favorite all books
INSERT INTO favorites (user_id, book_id) VALUE
(4,1),
(4,2),
(4,3),
(4,4),
(4,5);

-- all users who favorited thrid book
SELECT books.title, CONCAT_WS(' ', users.first_name, users.last_name) AS name FROM favorites
JOIN users ON favorites.user_id = users.id
JOIN books ON favorites.book_id = books.id
WHERE favorites.book_id = 3;

-- remove the first user of the 3rd's books favorites
DELETE FROM favorites
WHERE favorites.book_id = 3
ORDER BY favorites.user_id
LIMIT 1;

-- fifth user favorite the 2nd book
INSERT INTO favorites (user_id, book_id) VALUE (5,2);

-- all books third user favorited
SELECT users.id, CONCAT_WS(' ',users.first_name,users.last_name) AS name, books.title from books
JOIN favorites ON books.id = favorites.book_id
JOIN users ON favorites.user_id = users.id
WHERE users.id = 3;

-- all users that favorited the 5th book
SELECT books.title, CONCAT_WS(' ',users.first_name,users.last_name) FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN books on favorites.book_id = books.id
WHERE books.id = 5;