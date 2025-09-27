# 🏦 Bank Loan Case Study – Consumer Lending Analytics

_Analyzing loan portfolio performance and credit risk to support strategic lending decisions using Python, SQL, and Power BI._

[**🔗 View Interactive Power BI Dashboard**](https://app.powerbi.com/view?r=eyJrIjoiODI1YjZhYjEtNTE2MS00ZDBmLWFmM2MtNThlMmQxOGNhMTFhIiwidCI6ImRhNWM1MDFjLTBhMjQtNDNmNy04MWRmLTViNDcyZjA3ZjI2OSJ9)

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project analyzes consumer lending performance and credit risk to drive strategic insights for loan portfolio management, underwriting optimization, and risk assessment. A comprehensive data pipeline was built using Python for analysis and KPI calculations, SQL for data querying and metrics computation, and Power BI for interactive visualization.

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective loan portfolio management is critical in the lending industry. This project aims to:
- Track key portfolio KPIs including applications, funded amounts, and collection performance
- Analyze credit quality through good vs bad loan classification
- Monitor month-to-date (MTD) vs previous month-to-date (PMTD) trends
- Segment loan performance by geography, term, employment length, and purpose
- Optimize lending strategies through data-driven insights
- Support regulatory reporting and risk management decisions

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- **Loan applications data**: 38.6K total applications across multiple periods
- **Funded amount tracking**: $435.8M total portfolio value
- **Payment collections**: $473.1M received amount with performance tracking
- **Risk classifications**: Good loans (86.2%) vs Bad loans (13.8%)
- **Demographic segments**: State, employment length, home ownership, loan purpose

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- **Python** (Pandas, NumPy, Matplotlib, Seaborn) - Data analysis and KPI calculations
- **SQL** (Aggregate functions, CTEs, Window functions) - Data querying and metrics computation  
- **Power BI** (Interactive dashboards, DAX measures) - Visualization and reporting
- **Excel** (Data preparation and validation)
- **GitHub** (Version control and portfolio presentation)


---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- **Data Quality Checks**: Removed invalid records with missing loan IDs or amounts
- **Date Standardization**: Converted issue dates to proper datetime format for MTD calculations
- **Classification Logic**: Implemented good vs bad loan categorization based on loan status
- **Currency Formatting**: Standardized all financial figures to consistent decimal places
- **Outlier Treatment**: Handled extreme values in interest rates and DTI ratios
- **Missing Value Strategy**: Applied appropriate imputation for incomplete records

---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Portfolio Health Indicators:**
- **Total Applications**: 38.6K with 6.9% MoM growth
- **Funded Amount**: $435.8M with 13.0% MoM growth  
- **Collection Performance**: 108.6% collection ratio ($473.1M received vs $435.8M funded)

**Credit Quality Distribution:**
- **Good Loans**: 86.2% of portfolio (33,243 applications)
- **Bad Loans**: 13.8% charged-off rate (5,000 applications)
- **Interest Rate Patterns**: 12.0% average rate with risk-based pricing evident

**Geographic and Demographic Insights:**
- **State Concentration**: Uneven distribution requiring diversification strategy
- **Employment Length**: 10+ years category shows $116M funding (highest stability)
- **Loan Purpose**: Debt consolidation dominates at 52.8% of portfolio

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Portfolio Growth Trends**: 13.0% MoM funding growth with 15.8% collection growth indicating healthy expansion
2. **Credit Quality Management**: 86.2% good loan ratio demonstrates effective underwriting standards
3. **Term Structure Impact**: 60-month terms comprise 62.6% of portfolio, creating duration concentration risk
4. **Geographic Risk Distribution**: State-level analysis reveals market concentration requiring attention
5. **Employment Stability Correlation**: Longer employment history strongly correlates with loan performance
6. **Purpose-Based Performance**: Debt consolidation loans show different risk profile than other purposes
7. **Monthly Performance Acceleration**: Q4 shows significant growth acceleration in originations

---
<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

The Power BI dashboard provides comprehensive loan portfolio insights through three main views:

**📊 Summary Dashboard**: Executive KPI cards with MTD vs MoM comparisons
**📈 Overview Analytics**: Trend analysis, geographic distribution, and segment breakdowns  
**📋 Detailed Analysis**: Granular loan-level data with interactive filtering

Key visualizations include:
- Monthly funding trend analysis showing growth trajectory
- State-wise choropleth map for geographic insights
- Term distribution donut charts for portfolio composition
- Employment length and loan purpose segmentation
- Good vs bad loan performance comparison

![Overview Dashboard](https://github.com/shashankrawt-wq/Bank-Loan-analysis--Case-Study-Sql-Python-Power-BI/blob/03a8e4f7ba4d4721e029bf8865533fd916a6b37d/Dashboard%20Images/Overview.png)
![Loan Summary Dashboard](https://github.com/shashankrawt-wq/Bank-Loan-analysis--Case-Study-Sql-Python-Power-BI/blob/03a8e4f7ba4d4721e029bf8865533fd916a6b37d/Dashboard%20Images/Summary%20Dahboard.png)

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/bank-loan-case-study.git
cd bank-loan-case-study
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run data cleaning and preparation:**
```bash
python scripts/data_cleaning.py
python scripts/kpi_calculator.py
```

4. **Execute SQL analysis:**
- Run SQL scripts in `/sql/` folder against your database
- Execute `loan_kpis.sql` for main KPI calculations
- Run `segment_analysis.sql` for demographic breakdowns

5. **Open Jupyter notebooks:**
   - `notebooks/loan_data_analysis.ipynb` - Main analysis workflow
   - `notebooks/kpi_calculations.ipynb` - KPI computation logic
   - `notebooks/risk_segmentation_analysis.ipynb` - Segment deep-dives

6. **View Power BI Dashboard:**
   - Open `dashboard/Bank_Loan_Case_Study_Dashboard.pbix`
   - Or access the [live dashboard link](https://app.powerbi.com/view?r=eyJrIjoiODI1YjZhYjEtNTE2MS00ZDBmLWFmM2MtNThlMmQxOGNhMTFhIiwidCI6ImRhNWM1MDFjLTBhMjQtNDNmNy04MWRmLTViNDcyZjA3ZjI2OSJ9)

---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

**Portfolio Management:**
- Monitor the 13.8% bad loan rate for early warning indicators
- Diversify geographic concentration to reduce regional risk
- Balance term mix to optimize duration risk vs yield

**Credit Risk Optimization:**
- Leverage employment length insights for underwriting refinement
- Implement purpose-based risk pricing for debt consolidation loans
- Develop early warning systems based on MTD performance trends

**Business Intelligence Enhancement:**
- Expand dashboard with profitability metrics by segment  
- Implement automated alerting for KPI threshold breaches
- Add predictive analytics for portfolio performance forecasting

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**[Shashank Rawat]**  

📧 Email: [Shashankrawt@gmail.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/shashank-rawat-17033a272/)  


---

*This project demonstrates end-to-end analytics capabilities in the lending industry, showcasing proficiency in data analysis, SQL, Python, and Power BI for business intelligence and risk management applications.*70dd/Dashboard%20Screeshots.pdf)
