# WEEK 5 class

Introduction to `sqlite` for the creation and manipulation of databases. Sqlite
is the most widely used database system in the world (probably the most used
application overall) as it is included on all Android and iPhones as well as
many other devices including in highly regulated environments where integrity and stability are key.

It is lite in the sense that it is a small, fast and powerful
application that is usually embedded into applications/systems rather than
because it lacks capabilities.

It contrasts with traditional relation database management systems (RDBMS) that
required a *client - server* setup, where the database system typically runs on
a different computer server from the *client* application using the database.

Unlike RDBMS offering such as Oracle, DB2, SQLServer, mysql, etc., sqlite does not
include any user management or access permissions, and only supports one writer
at a time. Whilst it is suitable for running small websites that need read only
for all but the content manager of the site, it is generally not suitable for
multi-user applications. A sqlite database is stored in one file, which is highly portable.

sqlite is a much better alternative to *database by files* (which is an
application storing its own data in a collection of files to represent
different data structures, effectively storing a table of data in each file).

## Basic use
The current version of sqlite is 3.x. It has a shell that can be entered at the
command prompt with the command `sqlite3`.

In order to work with an existing database, or to create a new database, then
then then a filename should be given on the command line as well, preferably
ending with `.db` (the convention).

If no filename is specified on the command line, then everything done in sqlite
will be transitory and only exist for the duration of the sqlite session.

A file can be opened (created) from within sqlite using the `.OPEN` command,
e.g. `OPEN mydatabase.db` but this will lose anything done in session so far.

## Example session (this shows the commands only, not the responses)

sqlite myFirstDatabase.db

CREATE TABLE users(firstName TEXT, surName TEXT);
INSERT INTO users(firstName, surName) VALUES ('John','Smith');
INSERT INTO users(firstName, surName) VALUES ('Fred','Blogs');

SELECT oid, * from users;

INSERT INTO users(firstName, surName) VALUES ('Fred','Blogs');
INSERT INTO users VALUES ('Wendy','Blogs');

select oid, * from users;

update users set gender=male where oid=1;
update users set gender='male' where oid=1;

select oid, * from users;

update users set gender='Male' where oid=2;
update users set gender='Male' where oid=3;
update users set gender='Female' where oid=4;

select oid, * from users;

delete from users where oid=3;

select oid, * from users;

CREATE TABLE cars(make text, model text, colour text, userid integer);
.schema

INSERT INTO cars (make, model, colour, userid) VALUES ('Mercedes','S-Class', 'silver',1);
INSERT INTO cars (make, model, colour, userid) VALUES ('Skoda','Octavia Estate', 'blue',2);
INSERT INTO cars (make, model, colour, userid) VALUES ('BMW','Series 5', 'blue',3);
INSERT INTO cars (make, model, colour, userid) VALUES ('BMW','Series 3', 'green',2);

SELECT oid, * from cars;

SELECT u.firstName, u.surName, c.make, c.model, c.colour from users as u, cars as c;
SELECT u.firstName, u.surName, c.make, c.model, c.colour from users as u, cars as c where c.userid=u.userid;
SELECT u.firstName, u.surName, c.make, c.model, c.colour from users as u, cars as c where c.userid=u.oid;

UPDATE users set userid=3 where userid=3;
UPDATE cars set userid=3 where userid=3;

SELECT u.firstName, u.surName, c.make, c.model, c.colour from users as u, cars as c where c.userid=u.oid;

SELECT oid,* from cars;

UPDATE cars set userid=4 where userid=3;

SELECT oid,* from cars;

SELECT u.firstName, u.surName, c.make, c.model, c.colour from users as u, cars as c where c.userid=u.oid;

ALTER TABLE cars ADD COLUMN age integer;
ALTER TABLE cars ADD COLUMN miles integer;
UPDATE cars SET age=2 WHERE oid<2;

SELECT oid,* FROM cars;

INSERT INTO cars(make, model, colour, age, miles, userid) VALUES ('Ford','Fiesta','Black',5,32846,1);
INSERT INTO cars(make, model, colour, age, miles, userid) VALUES ('VW','Polo','Brown',6,22372,4);

.HEADERS on
.EXIT