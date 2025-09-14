## Loan Portfolio Analytics (Python + SQL + Power BI)

Overview
A compact, end-to-end analytics project for a consumer lending dataset. It computes portfolio and risk KPIs, performs segment analysis using SQL, and presents an interactive Power BI dashboard. The notebook reproduces KPI calculations and exports chart-ready data.

Repository Structure

notebooks/

Loan_Analysis.ipynb — Data prep, KPI calculations, chart exports.

sql/

Loan_Analysis_sql.sql — All KPI and segmentation queries.

dashboards/

Loan_Portfolio_Overview.pbix — Interactive dashboard.

reports/

Loan_KPIs_and_Charts.pdf — Static summary of visuals and insights.

data/ (optional) — Sample CSVs or connection notes, not tracked by default.

outputs/ (optional) — Exported CSVs for Power BI.

Dataset

Table: Bank_Loan_DB

Typical columns: id, issue_date, loan_status, loan_amount, total_payment, int_rate, dti, address_state, term, emp_length, purpose, home_ownership.

Data is not included. Add a small synthetic sample or provide DB connection instructions.

KPIs Implemented

Portfolio:

Total Loan Applications

Total Funded Amount

Total Amount Received

Average Interest Rate

Average DTI

Period Metrics:

MTD Applications, Funded Amount, Amount Received, Avg Interest, Avg DTI

PMTD equivalents for comparison

Credit Quality:

Good Loan % and Bad Loan %

Good/Bad Applications

Good/Bad Funded Amount

Good/Bad Amount Received

Segments:

Loan Status

Month

State

Term

Employment Length

Purpose

Home Ownership

SQL Reference (Loan_Analysis_sql.sql)

Totals and Periods:

Total applications, funded amount, amount received

MTD and PMTD metrics using MONTH(issue_date)

Average Interest Rate and Average DTI (multiplied by 100 for display)

Credit Quality:

Good Loans: loan_status IN ('Fully Paid', 'Current')

Bad Loans: loan_status = 'Charged Off'

Percentages and sums for each quality bucket

Loan Status Aggregates:

Counts, Total_Amount_Received, Total_Funded_Amount, Avg Interest, Avg DTI

MTD breakdown by loan_status

Segment Analyses:

By Month: MONTH(issue_date), DATENAME(MONTH, issue_date)

By State: address_state

By Term: term

By Employment Length: emp_length

By Purpose: purpose

By Home Ownership: home_ownership

Notebook (Loan_Analysis.ipynb)

Loads CSV/DB extracts, parses dates, cleans types

Recreates KPI tables and segment summaries

Exports chart-ready CSVs to outputs/ for Power BI

Optional: simple matplotlib visuals for validation

Power BI Dashboard (Loan_Portfolio_Overview.pbix)

Executive cards:

Good/Bad Loan %

Total Applications

Total Funded Amount

Total Amount Received

Avg Interest, Avg DTI

Visuals:

Monthly trend line/area

State bar chart

Term donut

Employment length bar

Purpose bar

Home ownership heat/tree map

Recommended slicers: Month, State, Term, Loan Status

How to Run

Clone

git clone https://github.com/<your-username>/<repo-name>.git

cd <repo-name>

Data

Option A: Connect to SQL Server with a Bank_Loan_DB table.

Option B: Export table to CSV (data/) and point the notebook to the file path.

SQL

Open sql/Loan_Analysis_sql.sql in SQL Server (or adapt MONTH/DATENAME for your RDBMS).

Run queries to validate metrics and generate result sets.

Python

Python 3.10+

pip install pandas numpy

Open notebooks/Loan_Analysis.ipynb and run cells.

Export CSVs to outputs/ if using Power BI with files.

Power BI

Open dashboards/Loan_Portfolio_Overview.pbix

Update data source to outputs/ CSVs or connect to your DB

Refresh visuals.

