use db_python;

create table table1(
	title varchar(500),
    hit int
    ) default charset=utf8;

drop table table1;
select * from table1;    
desc table1;
ALTER DATABASE db_python CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE table1 CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
alter table table1 change title title varchar(500) character set utf8mb4 collate utf8mb4_unicode_ci;