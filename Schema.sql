drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
create table robotInformation (
	id integer primary key autoincrement,
	climb boolean not null,
	'name' text not null
);
