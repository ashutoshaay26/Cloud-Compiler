create database cloudcompiler;


CREATE TABLE users(
	email VARCHAR(100) UNIQUE KEY NOT NULL,
    username VARCHAR(15) PRIMARY KEY,
    password VARCHAR(20) NOT NULL,
    isEmailVerified VARCHAR(1) NOT NULL DEFAULT 0,
    isAccountActive VARCHAR(1) NOT NULL DEFAULT 1,
    dateCreated TIMESTAMP NOT NULL DEFAULT NOW(),
    activation_key VARCHAR(64) NOT NULL
);

CREATE TABLE forgotPassword(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(100) NOT NULL,
    password_key VARCHAR(64) NOT NULL,
    timeRequested TIMESTAMP NOT NULL DEFAULT NOW(),
    isLinkActive VARCHAR(1) NOT NULL DEFAULT 1,
    timeChanged TIMESTAMP,
    isPasswordChanged VARCHAR(1) NOT NULL DEFAULT 0,
    
    FOREIGN KEY (email) REFERENCES users(email) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE repository(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(25) NOT NULL,
    username VARCHAR(15) NOT NULL,
    fileType VARCHAR(10) NOT NULL,
    timeCreated TIMESTAMP NOT NULL DEFAULT now(),
    pcid INT NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (pcid) REFERENCES pcip(pcid) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (fileType) REFERENCES languages(extension) ON DELETE RESTRICT ON UPDATE CASCADE    
);

CREATE TABLE languages(
    _language VARCHAR(10) NOT NULL PRIMARY KEY,
    extension VARCHAR(10) NOT NULL UNIQUE KEY
);

AlTER TABLE languages ADD COLUMN icon VARCHAR(150);

CREATE TABLE pcip(
	pcid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ip VARCHAR(20)  NOT NULL UNIQUE KEY    
);
INSERT INTO users (email,username,password) VALUES('harshmehta87.1997.hm@gmail.com','hgmehta','12345');
SELECT * FROM users;
SELECT * FROM forgotPassword;
SELECT * FROM repository;
DELETE FROM `cloudcompiler`.`users` WHERE `username`='harshmehta';
SELECT * FROM languages;
SELECT * FROM pcip;	

SELECT pcid FROM pcip WHERE ip = "10.20.24.15";

SELECT DISTINCT _language, TO_BASE64(fileType),fileType  FROM repository INNER JOIN languages ON languages.extension = repository.fileType WHERE username = 'harshmehta';
SELECT filename, fileType, 'harsh' , date(timeCreated),icon FROM repository INNER JOIN  languages ON languages.extension = repository.fileType WHERE username = 'harshmehta' AND filetype = 'py';

SELECT DISTINCT _language, COUNT(fileType),TO_BASE64(fileType)pcip, icon FROM repository INNER JOIN languages ON repository.fileType = languages.extension GROUP BY fileType;

SELECT * FROM repository WHERE filetype = 'py' AND id < 27  ORDER BY id DESC LIMIT 10;

set @row_num = 0;
SELECT id, filename, username, filetype, timeCreated, @row_num := @row_num + 1 as row_index FROM repository WHERE filetype = 'py' ORDER BY id DESC LIMIT 10;


-- UPDATE forgotPassword SET isLinkActive = '0', isPasswordChanged = '1', timeChanged = '2017-10-07 17:49:41.312178' WHERE email = 'harsh_m@hotmail.com' AND password_key = '7ad05a93993e860da600d797e627e833155b3219af223e7a346eeeb738fcfc23';