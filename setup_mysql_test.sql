-- Create the db 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Switch the db
USE hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privilege
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
