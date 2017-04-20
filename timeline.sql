CREATE TABLE Timeline
(
	year int,
	month int,
	day int,
	headline varchar(100),
	description varchar(5000),
	url varchar(200),
	caption varchar(200),
	credit varchar(200),
	PRIMARY KEY (headline)
);