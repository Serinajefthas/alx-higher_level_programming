-- Lists all privileges of MySQL users (user_0d_1, user_0d_2) on localhost
-- Scripts are run: cat 0-privileges.sql | mysql -hlocalhost -uroot -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
