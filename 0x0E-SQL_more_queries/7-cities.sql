-- Creates DB and table, with id in table (unique, auto-gen, cant be null and primary key) and name (can't be null) and state_id which is foreign key to id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
