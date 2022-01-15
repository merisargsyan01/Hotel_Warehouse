-- 1 Selected daily transaction amount and transaction count for each payment method.

SELECT to_date(b.transaction_date, 'yyyy-mm-dd') tarnsaction_date, pm."type" payment_method, 
SUM(b.amount) amount, Count(DISTINCT b.bill_id) transaction_count
FROM bill b
INNER JOIN payment_method pm ON b.payment_method_id = pm.payment_method_id
GROUP BY to_date(b.transaction_date, 'yyyy-mm-dd'), pm."type"
  

-- 2 Selected rooms reservation count and number of reserved rooms for each season.

SELECT extract(year FROM s.check_in) year_, CASE 
		WHEN extract(quarter FROM s.check_in) = 1
			THEN 'January-March'
		WHEN extract(quarter FROM s.check_in) = 2
			THEN 'April-June'
		WHEN extract(quarter FROM s.check_in) = 3
			THEN 'July-Sep'
		WHEN extract(quarter FROM s.check_in) = 4
			THEN 'Oct-Dec'
		END Season, count(s.room_id) reserved, count(DISTINCT s.room_id) room_count
FROM stay s
GROUP BY extract(year FROM s.check_in), extract(quarter FROM s.check_in)
ORDER BY 1, 2


-- 3 Selected customers that were active any 3 consecutive months.

SELECT DISTINCT b1.customer_id
FROM bill b1
JOIN bill b2 ON b2.customer_id = b1.customer_id
	AND DATEPART(month, b2.transaction_date) = DATEPART(month, b1.transaction_date) + 1
	AND DATEPART(year, b2.transaction_date) = DATEPART(year, b1.transaction_date)
JOIN bill b3 ON b3.customer_id = b1.customer_id
	AND DATEPART(month, b3.transaction_date) = DATEPART(month, b1.transaction_date) + 2
	AND DATEPART(year, b3.transaction_date) = DATEPART(year, b1.transaction_date)

	
	
--For checking the 3rd query
	
--DROP TABLE PUBLIC.test;

--CREATE TABLE test (customerId BIGINT, transactionDate DATE, amount BIGINT)
--
--INSERT INTO test VALUES (1, '2020-02-12', 1400);
--INSERT INTO test VALUES (1, '2020-02-13', 1401);
--INSERT INTO test VALUES (1, '2020-03-14', 1402);
--INSERT INTO test VALUES (1, '2020-04-15', 1403);
--INSERT INTO test VALUES (1, '2020-07-16', 1404);
--INSERT INTO test VALUES (2, '2020-01-17', 1405);
--INSERT INTO test VALUES (3, '2020-05-18', 1406);
--INSERT INTO test VALUES (3, '2020-06-19', 1407);
--INSERT INTO test VALUES (3, '2020-08-20', 1408);
--INSERT INTO test VALUES (4, '2020-04-21', 1409);
--INSERT INTO test VALUES (4, '2020-05-22', 1410);
--INSERT INTO test VALUES (4, '2020-06-23', 1411);
--INSERT INTO test VALUES (4, '2020-07-24', 1412);
--INSERT INTO test VALUES (5, '2020-02-25', 1413);
--INSERT INTO test VALUES (5, '2020-02-26', 1414);
--INSERT INTO test VALUES (6, '2020-02-27', 1415);
--INSERT INTO test VALUES (6, '2020-03-28', 1416);
--INSERT INTO test VALUES (6, '2020-04-29', 1417);
--INSERT INTO test VALUES (6, '2020-06-30', 1418);
--INSERT INTO test VALUES (6, '2020-08-31', 1419);
--INSERT INTO test VALUES (6, '2020-09-01', 1420);
--INSERT INTO test VALUES (6, '2020-10-02', 1421);
--INSERT INTO test VALUES (6, '2020-12-03', 1422);
--INSERT INTO test VALUES (6, '2020-12-04', 1423);
--INSERT INTO test VALUES (7, '2020-10-02', 1421);
--INSERT INTO test VALUES (7, '2020-11-03', 1422);
--INSERT INTO test VALUES (7, '2021-12-04', 1423);
--INSERT INTO test VALUES (8, '2021-10-02', 1421);
--INSERT INTO test VALUES (8, '2020-11-03', 1422);
--INSERT INTO test VALUES (8, '2021-12-04', 1423);
--
--SELECT * FROM test;
--
--SELECT DISTINCT b1.customerid 
--FROM test b1
--JOIN test b2 ON b2.customerid = b1.customerid
--	AND DATEPART(month, b2.transactiondate) = DATEPART(month, b1.transactiondate) + 1
--	AND DATEPART(year, b2.transactiondate) = DATEPART(year, b1.transactiondate)
--JOIN test b3 ON b3.customerid = b1.customerid
--	AND DATEPART(month, b3.transactiondate) = DATEPART(month, b1.transactiondate) + 2
--	AND DATEPART(year, b3.transactiondate) = DATEPART(year, b1.transactiondate)