-- create 6 new users
INSERT INTO users (first_name, last_name) VALUES
('amy', 'giver'),
('eli', 'byers'),
('marky', 'mark'),
('big', 'bird'),
('kermit', 'the frog'),
('buffalo', 'bill');

-- have user 1 be friends with user 2, 4, 6
INSERT INTO friendships (user_id, friend_id) VALUES
(1,2),
(1,4),
(1,6);

-- have user 2 be friends with user 1, 3, 5
INSERT INTO friendships (user_id, friend_id) VALUES
(2,1),
(2,3),
(2,5);

-- have user 3 be friends with user 2, 5
INSERT INTO friendships (user_id, friend_id) VALUES
(3,2),
(3,5);

-- have user 4 be friends with user 3
INSERT INTO friendships (user_id, friend_id) VALUES (4,3);

-- have user 5 be friends with user 1, 6
INSERT INTO friendships (user_id, friend_id) VALUES
(5,1),
(5,6);

-- have user 6 be friends with user 2, 3
INSERT INTO friendships (user_id, friend_id) VALUES
(6,2),
(6,3);

-- display the friendships
SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS users2 ON friendships.friend_id = users2.id;

-- display all users who are friends with first user
SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS users2 ON friendships.friend_id = users2.id
WHERE users.id = 1;

-- display count of all friendships
SELECT COUNT(*) AS 'friend_count' FROM friendships;

-- return user with most friends
SELECT CONCAT_WS(' ',users.first_name, users.last_name) AS name, COUNT(*) AS friend_count FROM users
JOIN friendships ON users.id = friendships.user_id
GROUP BY friendships.user_id
ORDER BY COUNT(*) DESC LIMIT 1;

-- return the friends of the third user
SELECT CONCAT_WS(' ',users.first_name, users.last_name) AS name, CONCAT_WS(' ',users2.first_name, users2.last_name) AS friend_name FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS users2 ON friendships.friend_id = users2.id
WHERE users.id = 3
ORDER BY users2.first_name;