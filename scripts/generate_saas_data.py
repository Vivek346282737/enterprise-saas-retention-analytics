import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Dimensions
tiers = [
    {"PlanID": 101, "PlanName": "Startup Cloud", "Tier": "Standard", "BaseMonthlyRate": 499},
    {"PlanID": 102, "PlanName": "Business Growth", "Tier": "Professional", "BaseMonthlyRate": 1499},
    {"PlanID": 103, "PlanName": "Enterprise Core", "Tier": "Enterprise", "BaseMonthlyRate": 4999},
    {"PlanID": 104, "PlanName": "Hyperscale Dedicated", "Tier": "Enterprise VIP", "BaseMonthlyRate": 12500}
]
df_plans = pd.DataFrame(tiers)
df_plans.to_csv("data/Dim_Plan.csv", index=False)

regions = ["North America", "EMEA", "APAC", "LATAM"]
industries = ["FinTech", "HealthTech", "Cybersecurity", "E-Commerce", "Enterprise AI"]

accounts = []
for i in range(1, 401):
    cohort_month = np.random.choice(["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"])
    accounts.append({
        "AccountID": f"ACC_{1000+i}",
        "AccountName": f"Client Entity {i}",
        "Region": np.random.choice(regions, p=[0.40, 0.28, 0.20, 0.12]),
        "Industry": np.random.choice(industries),
        "InitialCohortMonth": cohort_month,
        "AccountExecutive": f"exec_{(i%12)+1}@saasplatform.io"
    })
df_accounts = pd.DataFrame(accounts)
df_accounts.to_csv("data/Dim_Account.csv", index=False)

# Date Dimension
dates = pd.date_range(start="2025-01-01", end="2026-12-31", freq="D")
df_dates = pd.DataFrame({
    "DateKey": dates.strftime("%Y%m%d").astype(int),
    "FullDate": dates.strftime("%Y-%m-%d"),
    "Year": dates.year,
    "Quarter": "Q" + dates.quarter.astype(str),
    "Month": dates.month,
    "MonthYear": dates.strftime("%Y-%m"),
    "MonthName": dates.strftime("%b")
})
df_dates.to_csv("data/Dim_Date.csv", index=False)

# Subscription Fact Stream (MRR Ledger Events: New, Expansion, Contraction, Churn)
event_types = ["New Business", "Expansion", "Renewal", "Contraction", "Churn"]
ledger_events = []
current_date = datetime(2025, 1, 1)

total_records = 4200
for i in range(1, total_records + 1):
    acc = np.random.choice(accounts)
    plan = np.random.choice(tiers)
    event = np.random.choice(event_types, p=[0.35, 0.28, 0.22, 0.10, 0.05])
    
    random_days = np.random.randint(0, 680)
    tx_date = current_date + timedelta(days=random_days)
    if tx_date > datetime(2026, 11, 30):
        tx_date = datetime(2026, 11, 28)
        
    mrr_amount = plan["BaseMonthlyRate"]
    if event == "Expansion":
        mrr_amount = int(mrr_amount * np.random.choice([1.25, 1.5, 2.0]))
    elif event == "Contraction":
        mrr_amount = -int(mrr_amount * 0.4)
    elif event == "Churn":
        mrr_amount = -int(mrr_amount)
        
    arr_impact = mrr_amount * 12

    ledger_events.append({
        "TransactionID": f"TXN_{20000+i}",
        "DateKey": int(tx_date.strftime("%Y%m%d")),
        "AccountID": acc["AccountID"],
        "PlanID": plan["PlanID"],
        "EventType": event,
        "BillingCycle": np.random.choice(["Annual Prepaid", "Monthly Recurring"], p=[0.7, 0.3]),
        "MonthlyRecurringRevenue": mrr_amount,
        "AnnualRecurringRevenue": arr_impact,
        "LicenseSeats": np.random.randint(5, 250)
    })

df_fact = pd.DataFrame(ledger_events)
df_fact.to_csv("data/Fact_SubscriptionLedger.csv", index=False)

total_arr = df_fact[df_fact["EventType"] != "Churn"]["AnnualRecurringRevenue"].sum()
net_mrr = df_fact["MonthlyRecurringRevenue"].sum()

print(f"Data Generation Completed: {len(df_fact)} subscription transactions.")
print(f"Total Normalized ARR: ${total_arr:,.2f} | Net Monthly Run-Rate: ${net_mrr:,.2f}")
