# WEEK 5 class

Introduction to `sqlite` for the creation and manipulation of
databases. Sqlite is the most widely used database system in the
world (probably the most used application overall) as it is included
on all Android and iPhones as well as many other devices including
in highly regulated environments where integrity and stability are
key.

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

SQL statements need to end with a semi-colon `;`.

Note that sqlite is case insensitivei, other than for the content of text
fields, but by convention SQL commands are usually written in upppercase. In
addition, sqlite has some commands of its own that are preceded by a `.` and
these do need to be in lowercase and do not end with a semi-colon.

## Example sqlite session
Created a file, example.sql, that can be used to create a new database and add
make various changes, based on what was done in the week 5 class.

Invoke with the command: `sqlite3 test.db < example.sql`

Note: The test.db - or whatever name you choose - should not exist when you
invoke the script, or at least, should not contain the tables `users` and
`cars` or the script will suffer from errors.
