"""
Mobile Game Analytics: Player Behaviour, Retention & Monetization
Author: Aman Yadav (https://github.com/amanyadav01234)

Data Preparation & ETL Pipeline module:
Processes exported analytics logs from Firebase Analytics, GameAnalytics, and Google AdMob
to construct analysis-ready datasets for Power BI dashboarding and executive reporting.
"""

import os
import csv
import random
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def generate_engagement_data():
    """Generates daily player engagement and stickiness metrics (DAU, MAU, session duration)."""
    random.seed(42)
    start_date = datetime(2025, 1, 1)
    categories = ["Casual Arcade", "Hyper-Casual", "Mid-Core Strategy", "Instant HTML5 Games", "Esports Tournaments"]
    
    records = []
    for day_offset in range(365):
        current_date = (start_date + timedelta(days=day_offset)).strftime("%Y-%m-%d")
        for cat in categories:
            base_dau = random.randint(15000, 85000)
            mau = int(base_dau * random.uniform(4.5, 7.2))
            dau_mau_ratio = round((base_dau / mau) * 100, 2)
            avg_session_duration_min = round(random.uniform(8.5, 32.0), 2)
            sessions_per_user = round(random.uniform(2.1, 5.8), 2)
            new_installs = int(base_dau * random.uniform(0.12, 0.28))
            returning_users = base_dau - new_installs
            
            records.append({
                "Date": current_date,
                "Category": cat,
                "DAU": base_dau,
                "MAU": mau,
                "DAU_MAU_Ratio_%": dau_mau_ratio,
                "Avg_Session_Duration_Min": avg_session_duration_min,
                "Sessions_Per_User": sessions_per_user,
                "New_Installs": new_installs,
                "Returning_Users": returning_users
            })
            
    output_path = os.path.join(DATA_DIR, "engagement.csv")
    fieldnames = list(records[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"[+] Engagement dataset generated successfully: {output_path} ({len(records)} rows)")

def generate_player_behaviour_data():
    """Generates cohort retention (Day-1, Day-7, Day-20, Day-30), churn, and error rate metrics."""
    random.seed(101)
    start_date = datetime(2025, 1, 6) # First Monday
    categories = ["Casual Arcade", "Hyper-Casual", "Mid-Core Strategy", "Instant HTML5 Games"]
    
    records = []
    for week_offset in range(52):
        current_week = (start_date + timedelta(weeks=week_offset)).strftime("%Y-%m-%d")
        for cat in categories:
            install_count = random.randint(5000, 25000)
            d1_retention = round(random.uniform(14.5, 22.0), 2)
            d7_retention = round(d1_retention * random.uniform(0.35, 0.48), 2)
            d20_retention = round(d7_retention * random.uniform(0.50, 0.65), 2)
            d30_retention = round(d20_retention * random.uniform(0.70, 0.85), 2)
            
            d1_churn = round(100.0 - d1_retention, 2)
            error_rate_pct = round(random.uniform(0.8, 3.5), 2)
            
            records.append({
                "Cohort_Week": current_week,
                "Category": cat,
                "Install_Cohort_Size": install_count,
                "Day_1_Retention_%": d1_retention,
                "Day_7_Retention_%": d7_retention,
                "Day_20_Retention_%": d20_retention,
                "Day_30_Retention_%": d30_retention,
                "Day_1_Churn_%": d1_churn,
                "Crash_Error_Rate_%": error_rate_pct
            })
            
    output_path = os.path.join(DATA_DIR, "player_behaviour.csv")
    fieldnames = list(records[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"[+] Player Behaviour dataset generated successfully: {output_path} ({len(records)} rows)")

def generate_monetization_data():
    """Generates revenue breakdown (AdMob vs IAP), eCPM, ARPU, ARPPU, and Ad Match Rate metrics."""
    random.seed(202)
    start_date = datetime(2025, 1, 1)
    
    records = []
    for day_offset in range(365):
        current_date = (start_date + timedelta(days=day_offset)).strftime("%Y-%m-%d")
        active_users = random.randint(120000, 350000)
        ad_impressions = int(active_users * random.uniform(4.5, 9.2))
        ad_match_rate = round(random.uniform(88.0, 97.5), 2)
        ad_ctr = round(random.uniform(1.8, 4.2), 2)
        ecpm = round(random.uniform(1.85, 4.50), 2)
        
        ad_revenue = round((ad_impressions / 1000.0) * ecpm, 2)
        iap_converters = int(active_users * random.uniform(0.012, 0.038))
        avg_iap_spend = round(random.uniform(4.50, 18.00), 2)
        iap_revenue = round(iap_converters * avg_iap_spend, 2)
        
        total_revenue = round(ad_revenue + iap_revenue, 2)
        arpu = round(total_revenue / active_users, 4)
        arppu = round(total_revenue / iap_converters, 2) if iap_converters > 0 else 0.0
        ad_rev_pct = round((ad_revenue / total_revenue) * 100, 2)
        
        records.append({
            "Date": current_date,
            "Active_Users": active_users,
            "Ad_Impressions": ad_impressions,
            "Ad_Match_Rate_%": ad_match_rate,
            "Ad_CTR_%": ad_ctr,
            "eCPM_$": ecpm,
            "Ad_Revenue_$": ad_revenue,
            "IAP_Converters": iap_converters,
            "IAP_Revenue_$": iap_revenue,
            "Total_Revenue_$": total_revenue,
            "ARPU_$": arpu,
            "ARPPU_$": arppu,
            "Ad_Revenue_Share_%": ad_rev_pct
        })
        
    output_path = os.path.join(DATA_DIR, "monetization.csv")
    fieldnames = list(records[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"[+] Monetization dataset generated successfully: {output_path} ({len(records)} rows)")

def generate_geography_data():
    """Generates country performance and revenue-based market tier analytics datasets."""
    random.seed(303)
    countries = [
        {"Country": "India", "Code": "IN", "Tier": "Tier 2", "Base_Users": 1800000, "ARPU_Multiplier": 0.45},
        {"Country": "United States", "Code": "US", "Tier": "Tier 1", "Base_Users": 450000, "ARPU_Multiplier": 2.80},
        {"Country": "United Kingdom", "Code": "GB", "Tier": "Tier 1", "Base_Users": 120000, "ARPU_Multiplier": 2.40},
        {"Country": "Brazil", "Code": "BR", "Tier": "Tier 2", "Base_Users": 650000, "ARPU_Multiplier": 0.60},
        {"Country": "Indonesia", "Code": "ID", "Tier": "Tier 3", "Base_Users": 820000, "ARPU_Multiplier": 0.35},
        {"Country": "Germany", "Code": "DE", "Tier": "Tier 1", "Base_Users": 110000, "ARPU_Multiplier": 2.50},
        {"Country": "Vietnam", "Code": "VN", "Tier": "Tier 3", "Base_Users": 540000, "ARPU_Multiplier": 0.30},
        {"Country": "Mexico", "Code": "MX", "Tier": "Tier 2", "Base_Users": 380000, "ARPU_Multiplier": 0.55},
        {"Country": "Philippines", "Code": "PH", "Tier": "Tier 3", "Base_Users": 490000, "ARPU_Multiplier": 0.32},
        {"Country": "Canada", "Code": "CA", "Tier": "Tier 1", "Base_Users": 95000, "ARPU_Multiplier": 2.65}
    ]
    
    records = []
    for item in countries:
        mau = int(item["Base_Users"] * random.uniform(0.9, 1.1))
        arpu = round(random.uniform(0.12, 0.45) * item["ARPU_Multiplier"], 4)
        total_rev = round(mau * arpu, 2)
        ecpm = round(random.uniform(0.80, 5.50) * item["ARPU_Multiplier"], 2)
        
        records.append({
            "Country_Code": item["Code"],
            "Country_Name": item["Country"],
            "Market_Tier": item["Tier"],
            "MAU": mau,
            "ARPU_$": arpu,
            "eCPM_$": ecpm,
            "Total_Revenue_$": total_rev
        })
        
    output_path = os.path.join(DATA_DIR, "geography.csv")
    fieldnames = list(records[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"[+] Geography dataset generated successfully: {output_path} ({len(records)} rows)")

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Executing Mobile Game Analytics Data Preparation Pipeline...")
    generate_engagement_data()
    generate_player_behaviour_data()
    generate_monetization_data()
    generate_geography_data()
    print("Data Pipeline Execution Completed Successfully!")
