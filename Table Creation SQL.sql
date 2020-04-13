#create database major1db;
use major1db;

#create table stock_predicted(stkid varchar(20),stk_name varchar(20),stock_predictedcur_price float(20,5),pr_price float(20,5));

#insert into stock_predicted(stkid,stk_name) values(1,'AAPL');
#insert into stock_predicted(stkid,stk_name) values(2,'AMZN');
#insert into stock_predicted(stkid,stk_name) values(3,'F');
#insert into stock_predicted(stkid,stk_name) values(4,'FB');
#insert into stock_predicted(stkid,stk_name) values(5,'GOOG');
#insert into stock_predicted(stkid,stk_name) values(6,'IBM');
#insert into stock_predicted(stkid,stk_name) values(7,'INTC');
#insert into stock_predicted(stkid,stk_name) values(8,'MCD');
#insert into stock_predicted(stkid,stk_name) values(9,'MSFT');
#insert into stock_predicted(stkid,stk_name) values(10,'ORCL');

#UPDATE stock_predicted SET stk_name = 'AAPL' WHERE stkid = 1;
#UPDATE stock_predicted SET stk_name = 'AMZN' WHERE stkid = 2;

#create table market(stkid varchar(20),stk_name varchar(20),open_price float(20,5),close_price float(20,5),high float(20,5),low float(20,5),bid varchar(25),ask varchar(25),volume integer(12));

-- ALTER TABLE market MODIFY COLUMN stkid integer(5);

insert into market(stkid,stk_name) values(1,'AAPL');
insert into market(stkid,stk_name) values(2,'AMZN');
insert into market(stkid,stk_name) values(3,'F');
insert into market(stkid,stk_name) values(4,'FB');
insert into market(stkid,stk_name) values(5,'GOOG');
insert into market(stkid,stk_name) values(6,'IBM');
insert into market(stkid,stk_name) values(7,'INTC');
insert into market(stkid,stk_name) values(8,'MCD');
insert into market(stkid,stk_name) values(9,'MSFT');
insert into market(stkid,stk_name) values(10,'ORCL');