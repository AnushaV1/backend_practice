DROP DATABASE IF EXISTS  noyo_db;
CREATE DATABASE noyo_db;

\c noyo_db
DROP TABLE IF EXISTS users;
CREATE TABLE users
(
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(30) NOT NULL,
  middlename VARCHAR(30) NULL,
  lastname VARCHAR(30) NOT NULL,
  email TEXT UNIQUE NOT NULL,
  age INTEGER NOT NULL, 
  version_id INTEGER NOT NULL
);

CREATE TABLE users_old_version
(
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  firstname VARCHAR(30) NOT NULL,
  middlename VARCHAR(30) NULL,
  lastname VARCHAR(30) NOT NULL,
  email TEXT NOT NULL,
  age INTEGER NOT NULL, 
  version_id INTEGER NOT NULL
);


--INSERT INTO [Table to copy To]
--SELECT [Columns to Copy]
--FROM [Table to copy From]
--WHERE [Optional Condition];

--INSERT INTO users_old_version (user_id,firstname,middlename,lastname,email,age,version_id)
--SELECT id,firstname,middlename,lastname,email,age,version_id
--FROM users WHERE id = 1;

-- For testing - noyo_test_db

DROP DATABASE IF EXISTS  noyo_test_db;
CREATE DATABASE noyo_test_db;

\c noyo_test_db
DROP TABLE IF EXISTS users;
CREATE TABLE users
(
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(30) NOT NULL,
  middlename VARCHAR(30) NULL,
  lastname VARCHAR(30) NOT NULL,
  email TEXT UNIQUE NOT NULL,
  age INTEGER NOT NULL, 
  version_id INTEGER NOT NULL
);

CREATE TABLE users_old_version
(
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  firstname VARCHAR(30) NOT NULL,
  middlename VARCHAR(30) NULL,
  lastname VARCHAR(30) NOT NULL,
  email TEXT NOT NULL,
  age INTEGER NOT NULL, 
  version_id INTEGER NOT NULL
);

