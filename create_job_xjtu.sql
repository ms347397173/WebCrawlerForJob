--
-- Create the table children
--

use job;

CREATE TABLE job_xjtu_info(
		title varchar(128),
		time datetime,
		path varchar(128),
		url varchar(256),
		PRIMARY KEY (title)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;


