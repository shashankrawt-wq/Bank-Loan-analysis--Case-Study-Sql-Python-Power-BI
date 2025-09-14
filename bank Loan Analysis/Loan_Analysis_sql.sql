--Total Loan Applications

select count(*)
from Bank_Loan_DB


--MTD Loan Applications

select count(*) from Bank_Loan_DB
WHERE MONTH(issue_date) = 12



--Prev. MTD  Loan Applications
SELECT SUM(loan_amount) AS Total_Funded_Amount FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 11


--Total Amount Received

SELECT SUM(total_payment) AS Total_Amount_Collected FROM Bank_Loan_DB


--MTD Total Amount Received

SELECT SUM(total_payment) AS Total_Amount_Received FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 12

-- Prev. MTD Total Amount Received

SELECT SUM(total_payment) AS Total_Amount_Received FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 11


--Total Funded Amount
SELECT SUM(loan_amount) AS Total_Funded_Amount FROM Bank_Loan_DB

--MTD Total Funded Amount
SELECT SUM(loan_amount) AS Total_Funded_Amount FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 12


--Prev. MTD Total Funded Amount

SELECT SUM(loan_amount) AS Total_Funded_Amount FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 11

--Average Interest Rate

SELECT round(AVG(int_rate)*100,2) AS Avg_Int_Rate FROM Bank_Loan_DB

--MTD Average Interest

SELECT round(AVG(int_rate)*100,2) AS MTD_Avg_Int_Rate FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 12

-- Prev. MTD Average Interest

SELECT round(AVG(int_rate)*100,2) AS PMTD_Avg_Int_Rate FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 11



--Avg DTI
SELECT round(AVG(dti)*100,2) AS Avg_DTI FROM bank_loan_db


--MTD Avg DTI
SELECT round(AVG(dti)*100,2) AS MTD_Avg_DTI FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 12


-- Prev. MTD Avg DTI
SELECT round(AVG(dti)*100,2)
AS PMTD_Avg_DTI FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 11


--Good Loan Percentage
SELECT
    (COUNT(CASE WHEN loan_status = 'Fully Paid' OR loan_status = 'Current' THEN id END) * 100.0) / 
	COUNT(id) AS Good_Loan_Percentage
FROM Bank_Loan_DB



-- Good Loan Applications

SELECT COUNT(id) AS Good_Loan_Applications FROM Bank_Loan_DB
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'


-- Good Loan Funded Amount

SELECT SUM(loan_amount) AS Good_Loan_Funded_amount FROM Bank_Loan_DB
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'


-- Good Loan Amount Received


SELECT SUM(total_payment) AS Good_Loan_amount_received FROM Bank_Loan_DB
WHERE loan_status = 'Fully Paid' OR loan_status = 'Current'


--	Bad Loan Percentage

SELECT
    (COUNT(CASE WHEN loan_status = 'Charged Off' THEN id END) * 100.0) / 
	COUNT(id) AS Bad_Loan_Percentage
FROM Bank_Loan_DB


-- Bad Loan Applications

SELECT COUNT(id) AS Bad_Loan_Applications FROM Bank_Loan_DB
WHERE loan_status = 'Charged Off'


-- Bad Loan Funded Amount

SELECT SUM(loan_amount) AS Bad_Loan_Funded_amount FROM Bank_Loan_DB
WHERE loan_status = 'Charged Off'

--Bad Loan Amount Received

SELECT SUM(total_payment) AS Bad_Loan_amount_received FROM Bank_Loan_DB
WHERE loan_status = 'Charged Off'


-- Loan Status 

	SELECT
        loan_status,
        COUNT(id) AS LoanCount,
        SUM(total_payment) AS Total_Amount_Received,
        SUM(loan_amount) AS Total_Funded_Amount,
        AVG(int_rate * 100) AS Interest_Rate,
        AVG(dti * 100) AS DTI
    FROM
        Bank_Loan_DB
    GROUP BY
        loan_status


SELECT 
	loan_status, 
	SUM(total_payment) AS MTD_Total_Amount_Received, 
	SUM(loan_amount) AS MTD_Total_Funded_Amount 
FROM Bank_Loan_DB
WHERE MONTH(issue_date) = 12 
GROUP BY loan_status


-- MONTH
SELECT 
	MONTH(issue_date) AS Month_Munber, 
	DATENAME(MONTH, issue_date) AS Month_name, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM Bank_Loan_DB
GROUP BY MONTH(issue_date), DATENAME(MONTH, issue_date)
ORDER BY MONTH(issue_date)



-- State


SELECT 
	address_state AS State, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM bank_loan_DB
GROUP BY address_state
ORDER BY address_state


-- Term


SELECT 
	term AS Term, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM Bank_Loan_DB	
GROUP BY term
ORDER BY term


--  EMPLOYEE LENGTH

SELECT 
	emp_length AS Employee_Length, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM Bank_Loan_DB
GROUP BY emp_length
ORDER BY emp_length



-- Purpose

SELECT 
	purpose AS PURPOSE, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM Bank_Loan_DB
GROUP BY purpose
ORDER BY purpose

--Home Ownership

SELECT 
	home_ownership AS Home_Ownership, 
	COUNT(id) AS Total_Loan_Applications,
	SUM(loan_amount) AS Total_Funded_Amount,
	SUM(total_payment) AS Total_Amount_Received
FROM Bank_Loan_DB
GROUP BY home_ownership
ORDER BY home_ownership


