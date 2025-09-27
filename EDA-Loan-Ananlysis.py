import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
df = pd.read_excel(r"C:\\Users\\shashank\\OneDrive\\Desktop\\financial_loan_data_excel.xlsx")
#no. of rows and columns
df.shape
#top 5 rows
df.head()
#last 5 rows

df.tail()
#datatpes
df.dtypes
#summary
df.describe()
total_loan_application=df['id'].count()
print(total_loan_application)
lat_date = df['issue_date'].max()
lat_year = lat_date.year
lat_month = lat_date.month

mtd_data = df[(df['issue_date'].dt.year == lat_year) & (df['issue_date'].dt.month == lat_month)]

mtd_loan_applications = mtd_data['id'].count()

print(f"MTD Loan Applications (for {lat_date.strftime('%B %Y')}): {mtd_loan_applications}")
total_funded_amount=df['loan_amount'].sum()
print("total Funded Amount is",total_funded_amount)
#total funded amount in million 

total_funded_amount_million=total_funded_amount/1000000
print("total Funded Amount in Millions is ${:.2f}M".format(total_funded_amount_million))
mtd_total_funded_amount=mtd_data['loan_amount'].sum()
mtd_total_funded_amount_million=mtd_total_funded_amount/1000000
print("total funded amount is",mtd_total_funded_amount)
print("total funded amount in million is ${:.2f}M".format(mtd_total_funded_amount_million))
total_amount_received=df['total_payment'].sum()
total_amount_received_million=total_amount_received/1000000
print('total amount received is', total_amount_received)
print('total amount received  million ${:.2f}M'.format(total_amount_received_million))
mtd_total_amount_received=mtd_data['total_payment'].sum()
mtd_total_amount_received_million=mtd_total_amount_received/1000000
print('mtd total amount received',mtd_total_amount_received)
print('mtd total amount received in millions is ${:.2f}M'.format(mtd_total_amount_received_million))
avg_interest_rate=df['int_rate'].mean()*100
print ('average interest rate is {:.2f}%'.format(avg_interest_rate))
avg_DTI=df['dti'].mean()*100
print ('average DTI is {:.2f}%'.format(avg_DTI))
# Filter good loans by status
good_loans = df[df['loan_status'].isin(["Fully Paid", "Current"])]

# Total loan applications
total_loan_applications = df['id'].count()

# Good loan metrics
good_loan_applications = good_loans['id'].count()
good_loan_funded_amount = good_loans['loan_amount'].sum()
good_loan_received = good_loans['total_payment'].sum()

# Convert amounts to millions
good_loan_funded_amount_millions = good_loan_funded_amount / 1_000_000
good_loan_received_millions = good_loan_received / 1_000_000

# Good loan application percentage
good_loan_percentage = (good_loan_applications / total_loan_applications) * 100

# Print results
print("Good Loan Applications:", good_loan_applications)
print(
    "Good Loan Funded Amount (in Millions): ${:.2f}M"
    .format(good_loan_funded_amount_millions)
)
print(
    "Good Loan Total Received (in Millions): ${:.2f}M"
    .format(good_loan_received_millions)
)
print(
    "Percentage of Good Loan Applications: {:.2f}%"
    .format(good_loan_percentage)
)
# Filter bad loans by status
bad_loans = df[df['loan_status'].isin(['Charged Off'])]

# Total loan applications
total_loan_applications = df['id'].count()

# bad loan metrics
bad_loan_applications = bad_loans['id'].count()
bad_loan_funded_amount = bad_loans['loan_amount'].sum()
bad_loan_received = bad_loans['total_payment'].sum()

# Convert amounts to millions
bad_loan_funded_amount_millions = bad_loan_funded_amount / 1_000_000
bad_loan_received_millions = bad_loan_received / 1_000_000

# bod loan application percentage
bad_loan_percentage = (good_loan_applications / total_loan_applications) * 100

# Print results
print("bad Loan Applications:", bad_loan_applications)
print(
    "bad Loan Funded Amount (in Millions): ${:.2f}M"
    .format(bad_loan_funded_amount_millions)
)
print(
    "bad Loan Total Received (in Millions): ${:.2f}M"
    .format(bad_loan_received_millions)
)
print(
    "Percentage of bad Loan Applications: {:.2f}%"
    .format(bad_loan_percentage)
)
# Aggregate funded amount by month and convert to millions
monthly_funded = (
    df.sort_values('issue_date')
      .assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y'))
      .groupby('month_name', sort=False)['loan_amount']
      .sum()
      .div(1_000_000)
      .reset_index(name='loan_amount_millions')
)

# Plot area + line chart with labels
plt.figure(figsize=(10, 5))
plt.fill_between(
    monthly_funded['month_name'],
    monthly_funded['loan_amount_millions'],
    color='violet',
    alpha=0.5
)
plt.plot(
    monthly_funded['month_name'],
    monthly_funded['loan_amount_millions'],
    color='Purple',
    linewidth=2
)

# Value labels on each point
for i, row in monthly_funded.iterrows():
    plt.text(
        i,
        row['loan_amount_millions'] + 0.1,
        f"{row['loan_amount_millions']:.2f}",
        ha='center',
        va='bottom',
        fontsize=9,
        rotation=0,
        color='black'
    )

plt.title('Total Funded Amount by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Funded Amount (₹ Millions)')
plt.xticks(ticks=range(len(monthly_funded)), labels=monthly_funded['month_name'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# Monthly Applications: aggregate counts by issue month
monthly_amount_received = (
    df.sort_values('issue_date')
      .assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y'))
      .groupby('month_name', sort=False)['total_payment']
      .sum()
      .div(1000000)  # convert to millions
      .reset_index(name='received_amount_million')
)

# Prepare x and y values
x = range(len(monthly_amount_received))
y = monthly_amount_received['received_amount_million']

# Plot: filled area + line for monthly application counts
plt.figure(figsize=(10, 5))
plt.fill_between(
    monthly_amount_received['month_name'],
    monthly_amount_received['received_amount_million'],
    color='Orange',
    alpha=0.5)
plt.plot(monthly_amount_received['month_name'], monthly_amount_received['received_amount_million'], color='DarkOrange', linewidth=2)

# Add value labels above each point
for i, val in enumerate(y):
    plt.text(
        i, val + 0.5,
        f"{val:.2f}",  # show 2 decimal places
        ha='center',
        va='bottom',
        fontsize=9,
        color='black'
    )

plt.title('Total Amount Received by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Amount Received (₹ Millions)')
plt.xticks(ticks=x, labels=monthly_amount_received['month_name'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
# Monthly Applications: aggregate counts by issue month
monthly_applications = (
    df.sort_values('issue_date')
      .assign(month_name=lambda x: x['issue_date'].dt.strftime('%b %Y'))
      .groupby('month_name', sort=False)['id']
      .count()
      .reset_index(name='loan_applications_count')
)

# Plot: filled area + line for monthly application counts
plt.figure(figsize=(10, 5))
plt.fill_between(
    monthly_applications['month_name'],
    monthly_applications['loan_applications_count'],
    color='LightBlue',
    alpha=0.5
)
plt.plot(
    monthly_applications['month_name'],
    monthly_applications['loan_applications_count'],
    color='blue',
    linewidth=2
)

# Add value labels above each point
for i, row in monthly_applications.iterrows():
    plt.text(
        i,
        row['loan_applications_count'] + 0.5,
        f"{row['loan_applications_count']}",
        ha='center',
        va='bottom',
        fontsize=9,
        rotation=0,
        color='black'
    )

plt.title('Total Loan Applications by Month', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Number of Applications')
plt.xticks(
    ticks=range(len(monthly_applications)),
    labels=monthly_applications['month_name'],
    rotation=45
)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

state_funding = df.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True)
state_funding_thousands = state_funding / 1000

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(state_funding_thousands.index, state_funding_thousands.values, color='lightGreen')

# Add value labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:.0f}K', va='center', fontsize=9)

plt.title('Total Funded Amount by State (in ₹ Thousands)')
plt.xlabel('Funded Amount (₹ \'000)')
plt.ylabel('State')
plt.tight_layout()
plt.show()
state_amount_received = df.groupby('address_state')['total_payment'].sum().sort_values(ascending=True)
state_amount_received_thousands = state_amount_received / 1000

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(state_amount_received_thousands.index, state_amount_received_thousands.values, color='lightPink')

# Add value labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:.0f}K', va='center', fontsize=9)

plt.title('Total Amount Received by State (in ₹ Thousands)')
plt.xlabel(' Amount Received (₹ \'000)')
plt.ylabel('State')
plt.tight_layout()
plt.show()
state_loan_application = df.groupby('address_state')['id'].count().sort_values(ascending=True)
state_loan_application_thousands = state_loan_application / 1000

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(state_loan_application_thousands.index, state_loan_application.values, color='red')

# Add value labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:.0f}', va='center', fontsize=9)

plt.title('Total Loan Applications By State)')
plt.xlabel(' Total Loan Applications')
plt.ylabel('State')
plt.tight_layout()
plt.show()
term_funding_millions = df.groupby('term')['loan_amount'].sum() / 1000000

plt.figure(figsize=(5, 5))
plt.pie(
    term_funding_millions,
    labels=term_funding_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*sum(term_funding_millions)/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4}
)
plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total Funded Amount by Term (in $ Millions)")
plt.show()
amount_received_millions = df.groupby('term')['total_payment'].sum() / 1000000

# Define custom colors - green and red
colors = ['#ff6b6b', '#51cf66', '#ff6b6b', '#51cf66', '#ff6b6b']

plt.figure(figsize=(5, 5))
plt.pie(
    amount_received_millions,
    labels=amount_received_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*sum(amount_received_millions)/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4},
    colors=colors  # Using green and red colors
)
plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total Amount Received By Term (in $ Millions)")
plt.show()
terms_loan_application = df.groupby('term')['id'].count()

# Define custom colors - purple and black
colors = ['#800080', '#000000', '#800080', '#000000', '#800080']

plt.figure(figsize=(5, 5))
plt.pie(
    terms_loan_application,
    labels=terms_loan_application.index,
    autopct=lambda p: f"{p:.1f}%\n{p*sum(terms_loan_application)/100:.0f}",
    startangle=90,
    wedgeprops={'width': 0.4},
    colors=colors  # Using purple and black colors
)
plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total Loan Application by Term")
plt.show()
emp_funding = df.groupby('emp_length')['loan_amount'].sum().sort_values() / 1000000

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_funding.index, emp_funding, color='purple')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"${width:.0f}M", va='center', fontsize=9)

plt.xlabel("Funded Amount ($ Thousands)")
plt.title("Total Funded Amount by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
emp_amount_received = df.groupby('emp_length')['total_payment'].sum().sort_values() / 1000000

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_amount_received.index, emp_amount_received, color='purple')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"${width:.0f}M", va='center', fontsize=9)

plt.xlabel("Amount Received ($ Millions)")
plt.title("Total Amount Received by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
emp_loan_application = df.groupby('emp_length')['id'].count().sort_values() 

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_loan_application.index, emp_loan_application, color='pink')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"{width:.0f}", va='center', fontsize=9)

plt.xlabel("Loan Applications")
plt.title("Total Loan applications by Employee Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
purpose_funding_millions = (df.groupby('purpose')['loan_amount'].sum().sort_values() / 1000000)

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_funding_millions.index, purpose_funding_millions.values, color='LightGreen')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}M', va='center', fontsize=9)

plt.title('Total Funded Amount by Loan Purpose ($ Millions)', fontsize=14)
plt.xlabel('Funded Amount ($ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
purpose_received_amount = (df.groupby('purpose')['total_payment'].sum().sort_values() / 1000000)

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_received_amount.index, purpose_received_amount.values, color='skyblue')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}M', va='center', fontsize=9)

plt.title('Total Received Amount by Loan Purpose ($ Millions)', fontsize=14)
plt.xlabel('Amount Received ($ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
purpose_loan_application = (df.groupby('purpose')['id'].count().sort_values() )

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_loan_application.index, purpose_loan_application.values, color='Lime')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.0f}', va='center', fontsize=9)

plt.title('Total Loan Applications by Loan Purpose', fontsize=14)
plt.xlabel('Total Loan Applications')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
home_funding = df.groupby('home_ownership')['loan_amount'].sum().reset_index()
home_funding['loan_amount_millions'] = home_funding['loan_amount'] / 1_000_000

fig = px.treemap(
    home_funding,
    path=['home_ownership'],
    values='loan_amount_millions',
    color='loan_amount_millions',
    color_continuous_scale='Reds',
    title='Total Funded Amount by Home Ownership ($ Millions)'
)

fig.show()
home_received_amount = df.groupby('home_ownership')['total_payment'].sum().reset_index()
home_received_amount['Received_Amount_millions'] = home_received_amount['total_payment'] / 1_000_000

fig = px.treemap(
    home_received_amount,
    path=['home_ownership'],
    values='Received_Amount_millions',
    color='Received_Amount_millions',
    color_continuous_scale='greens',
    title='Total Received Amount by Home Ownership ($ Millions)'
)

fig.show()
home_loan_applicantion= df.groupby('home_ownership')['id'].count().reset_index()
home_loan_applicantion['total_loan_application'] = home_loan_applicantion['id'] 

fig = px.treemap(
    home_loan_applicantion,
    path=['home_ownership'],
    values='total_loan_application',
    color='total_loan_application',
    color_continuous_scale='greens',
    title='Total Loan Application by Home Ownership '
)

fig.show()
%history f- EDA-Loan-Ananlysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly.express as px
df = pd.read_excel(r"C:\\Users\\shashank\\OneDrive\\Desktop\\financial_loan_data_excel.xlsx")
#no. of rows and columns
df.shape
%history -f EDA-Loan-Ananlysis.py
