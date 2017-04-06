/* SQLite example script based on WEEK 5 class
 *
 * Make sure test database does not exist then invoke with
 *
 * sqlite3 testdatabasename.db < example.sql
 *
 * The script leaves you back at the command prompt (exits from sqlite) after
 * running. You can open a new session to work on the database if desired.
 */
--
-- turn echo on so commands rather just outputs are shown
--
.echo on

--
-- create our first table, and add two rows (records) of data to the table
--
CREATE TABLE users(firstName TEXT, surName TEXT); -- two columns (fields)
INSERT INTO users(firstName, surName) VALUES ('John','Smith');
INSERT INTO users(firstName, surName) VALUES ('Kevin','Blogs');

--
-- output all records, showing all (the *) of the declared fields
--
SELECT oid, * from users; -- also show the oid, the automatic row index number

--
-- add some more records
--
INSERT INTO users(firstName, surName) VALUES ('Fred','Blogs');
INSERT INTO users VALUES ('Wendy','Blogs'); -- assumes values are in order

--
-- add an extra column (field)
--
ALTER TABLE users ADD COLUMN gender TEXT;

--
-- a sqlite command to show the structure of the database
--
.schema

--
-- show current table content (nothing shown for gender as still empty)
--
SELECT oid, * FROM users;

--
-- do an update that changes only records meeting specified criteria
--
UPDATE users SET gender='Male' WHERE oid=1;

--
-- show all records, so can see the change
--
SELECT oid, * FROM users;

--
-- set gender of remaining records
--
UPDATE users SET gender='Male' WHERE oid=2;
UPDATE users SET gender='Male' WHERE oid=3;
UPDATE users SET gender='Female' WHERE oid=4;

--
-- add some more records for test purposes
--
INSERT INTO users VALUES('Helen','Doe','Female');
INSERT INTO users VALUES('Steve','Brown','Unknown');

--
-- show all records so we can see how we are doing
--
SELECT oid, * FROM users;

--
-- the delete command is used to remove specific records
--
DELETE FROM users WHERE oid=3;

--
-- show all records so we can see one was deleted
--
SELECT oid, * FROM users;

--
-- create second table, add records; userid corresponds to oid in first table
--
CREATE TABLE cars(make text, model text, colour text, userid integer);
INSERT INTO cars (make, model, colour, userid) VALUES ('Mercedes','S-Class', 'silver',1);
INSERT INTO cars (make, model, colour, userid) VALUES ('Skoda','Octavia Estate', 'blue',2);
INSERT INTO cars (make, model, colour, userid) VALUES ('BMW','Series 5', 'blue',5);
INSERT INTO cars (make, model, colour, userid) VALUES ('BMW','Series 3', 'green',4);
INSERT INTO cars (make, model, colour, userid) VALUES ('VW','Series 3', 'green',6);
INSERT INTO cars (make, model, colour, userid) VALUES ('Ford','Fiesta', 'green',2);
INSERT INTO cars (make, model, colour, userid) VALUES ('Audi','A5', 'green',6);

--
-- issue sqlite dot command to output headers before data
--
.headers on
SELECT oid, * FROM cars;  -- show all records

--
-- look at all records in combination from two tables
--
SELECT u.firstName, u.surName, c.make, c.model, c.colour FROM users AS u, cars AS c;
/* ^^^ that repeats every entry from first table against every entry from
 *     second table, which is not the desired outcome
 */

--
--     a WHERE clause is required to link userid of cars with oid of users
--
SELECT u.firstName, u.surName, c.make, c.model, c.colour FROM users AS u, cars AS c WHERE c.userid=u.oid;

--
-- add some more columns, and just for example assign some data
--
ALTER TABLE cars ADD COLUMN age integer;
ALTER TABLE cars ADD COLUMN miles integer;
.schema

--
-- update the new columns for example purposes
--
UPDATE cars SET age=2, miles=30000 WHERE oid<=3;
UPDATE cars SET age=4, miles=50000  WHERE oid>=4;

--
-- add records, not using VALUES on own as want to specify data in diff order
--
INSERT INTO cars(make, model, colour, age, miles, userid) VALUES ('Ford','Fiesta','Black',5,32846,1);
INSERT INTO cars(make, model, colour, age, miles, userid) VALUES ('VW','Polo','Brown',6,22372,4);

--
-- issue sqlite dot command to output data in column format
--
.mode column

--
-- and to get sorted output, use ORDER BY (and notice line can be split up)
--
SELECT u.firstName, u.surName, c.make, c.model, c.colour
    FROM users AS u, cars AS c
    WHERE c.userid=u.oid
    ORDER BY u.firstName;

/* delete corresponding records from both tables, and output revised tables
 * (there are better ways to do this, using joins and foreign keys)
 */

--
-- firstly, remove a specific user record
--
DELETE FROM users WHERE oid=4;

--
-- secondly, remove all cars that lack a corresponding user in users
--
DELETE FROM cars  WHERE userid NOT IN (SELECT DISTINCT oid FROM users);

SELECT u.firstName, u.surName, c.make, c.model, c.colour
    FROM users AS u, cars AS c
    WHERE c.userid=u.oid
    ORDER BY u.firstName;

--
-- end of script, exiting sqlite. Start a new session to work with database.
--
