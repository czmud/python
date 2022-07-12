-- create 3 new dojos
INSERT INTO dojos (name) VALUES
('dojo1'),
('dojo2'),
('dojo3');
-- delete dojos
DELETE FROM dojos WHERE id = 1 OR id = 2 OR id = 3;
-- create 3 more dojos
INSERT INTO dojos (name) VALUES
('dojo4'),
('dojo5'),
('dojo6');
-- create 3 ninjas in each of the 3 dojos
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES
('mike', 'edwards', 43, 4),
('drew', 'kim', 27, 4),
('felipe', 'aguilera', 33, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES
('mike', 'edwards', 43, 5),
('drew', 'kim', 27, 5),
('felipe', 'aguilera', 33, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES
('mike', 'edwards', 43, 6),
('drew', 'kim', 27, 6),
('felipe', 'aguilera', 33, 6);
-- retrieve all ninjas in first dojo
SELECT * FROM ninjas WHERE dojo_id = 4;
-- retried all ninjas in last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;
-- retrieve the dojo for the last ninja
SELECT dojos.name FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
ORDER BY ninjas.id DESC LIMIT 1;