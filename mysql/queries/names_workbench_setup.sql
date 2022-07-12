-- show all names in database
SELECT * FROM names;
-- insert my own name into database
INSERT INTO names (name) VALUES ('caleb zmuda'); 
-- insert list of more names into database
INSERT INTO names (name) VALUES
('sean sedlack'),
('billy savage'),
('keith grendon'),
('sally chen'); 
-- optional: try creating, updating, deleting entries
-- update sally's name to 'sally tao'
UPDATE names SET name = 'sally tao' WHERE id = 5;
-- delet billy from database
DELETE FROM names WHERE id = 3;