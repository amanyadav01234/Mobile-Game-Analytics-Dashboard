# Mobile Game Analytics: Player Behaviour, Retention & Monetization

**Author**: [Aman Yadav](https://github.com/amanyadav01234)  
**GitHub Profile**: [github.com/amanyadav01234](https://github.com/amanyadav01234)  

An end-to-end data analytics and Power BI project focused on understanding how players engage with a mobile game, how long they stay, how the game generates revenue, and how performance varies across markets.

---

## About the Project

This project was developed as a comprehensive business intelligence and product analytics solution for a mobile game publisher.

The goal was to bring together data from multiple analytics sources and turn it into a more useful view of overall game performance, unit economics, and strategic growth drivers.

The analysis focuses on four main areas:

- **Player engagement**
- **Player retention and churn**
- **Monetization and advertising performance**
- **Geographic performance & market tiers**

I used **Python** to prepare, transform, and model the data, then built an interactive **Power BI dashboard** and strategic growth framework to explore the results and identify actionable business insights.

---

## What I Worked On

The project followed an end-to-end analytics and growth workflow:

**Data Sources → Python ETL → Data Preparation → Financial & Retention Modeling → Power BI → DAX → Dashboard → Business Strategy**

### Data Preparation & Pipeline

The project started with exported raw CSV data from Firebase Analytics, GameAnalytics, and Google AdMob.

Using Python, pandas, and NumPy, I:

- Inspected the datasets and their underlying schema structure
- Checked for duplicate records and handled missing values
- Standardized date fields and timestamp formats
- Reviewed data consistency across analytics tools
- Created additional analytical fields (DAU/MAU ratio, churn rates, eCPM)
- Calculated ARPU, ARPPU, and returning-user percentages
- Created revenue-based market tiers (Tier 1, Tier 2, Tier 3)
- Prepared four analysis-ready datasets and engineered dynamic P&L & retention models

The final core datasets cover:

- **Engagement** (`data/engagement.csv`)
- **Player Behaviour** (`data/player_behaviour.csv`)
- **Monetization** (`data/monetization.csv`)
- **Geography** (`data/geography.csv`)

---

## Power BI Dashboard

The Power BI dashboard is organized into four interactive pages.

### 1. Executive Overview

Provides a high-level view of overall game performance using executive KPIs and trend visuals such as:

- ARPU (Average Revenue Per User)
- Day-1 and Day-7 retention rates
- DAU/MAU stickiness ratio
- eCPM (Effective Cost Per Mille)
- Total revenue breakdown
- Monthly Active Users (MAU)
- New vs. returning user composition
- Weekly revenue trends

![Executive Overview](dashboard/01-executive-overview.png)

---

### 2. Player Behaviour

Focuses on player retention curves, onboarding funnels, and churn rates across install cohorts.

It includes:

- Day-1 retention %
- Day-7 retention %
- Day-20 retention %
- Retention decay curve
- Churn rate analytics
- Technical crash/error rate by cohort day

![Player Behaviour](dashboard/02-player-behaviour.png)

---

### 3. Monetization

Looks at how the game generates revenue and how effectively advertising & in-app purchases perform.

The dashboard includes:

- ARPU & ARPPU trends
- Ad impressions & match rate
- Ad CTR (Click-Through Rate %)
- eCPM by ad format
- Weekly revenue trajectory
- Advertising vs. In-App Purchase (IAP) revenue split

![Monetization](dashboard/03-monetization.png)

---

### 4. Geography

Explores game performance and monetization efficiency across different countries and market tiers.

It includes:

- Global countries represented
- Revenue by country
- ARPU by country
- Top 10 revenue-generating countries
- Revenue-based market tiers (Tier 1, Tier 2, Tier 3)
- Interactive cross-filtering

![Geography](dashboard/04-geography.png)

---

## Key Findings & Strategic Insights

The dashboard highlighted several critical areas for product optimization and growth.

### Player Engagement
DAU/MAU showed a gradual decline during the year, indicating that overall player stickiness was weakening over time and requiring retention-focused feature updates.

### Retention Bottlenecks
The largest player drop-off occurred immediately after installation. **Day-1 churn was approximately 85.5%**, making early player experience (FTUE) and onboarding friction reduction a primary area for growth.

### Monetization Mix
The game was heavily dependent on advertising, with approximately **99.6% of revenue coming from ads** in the analyzed data. Implementing a hybrid monetization model (IAP / Battle Pass + Rewarded Ads) provides significant ARPU uplift potential.

### Geographic Yield
Revenue per player varied substantially across market tiers. Comparing revenue with active user volume helped isolate high-eCPM Tier 1 markets (US, UK, DE) for ad mediation optimization versus high-volume Tier 2 markets (India, Brazil) for micro-transaction expansion.

---

## Power BI Data Model

The four datasets have different levels of detail, including daily, weekly, cohort-day, and country-level data.

![Power BI Data Model](dashboard/05-powerbi-data-model.png)

To avoid creating incorrect relationships between unrelated tables, I used a shared **Calendar dimension** to support consistent date-based filtering across the data model.

The dashboard is powered by DAX measures for metrics including:

- Total Revenue
- Average ARPU
- Average ARPPU
- Average eCPM
- Ad Revenue %
- DAU/MAU Ratio
- Day-1 Retention
- Day-7 Retention
- Day-20 Retention
- Churn Rate

*A complete reference of DAX formulas is available in [`dax/DAX_Measures.md`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/dax/DAX_Measures.md).*

---

## Python Analytics & Growth Modeling (`src/`)

In addition to the Power BI dashboard, I built a modular Python analytics suite for data engineering, unit economics modeling, and funnel optimization:

- **[`src/data_pipeline.py`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/src/data_pipeline.py)**: Automated data ETL pipeline processing raw analytics logs into clean CSV datasets.
- **[`src/pnl_unit_economics.py`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/src/pnl_unit_economics.py)**: P&L financial optimizer evaluating Gross Margin %, COGS, blended CAC, user LTV, and revenue growth scenarios.
- **[`src/funnel_retention_analysis.py`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/src/funnel_retention_analysis.py)**: Onboarding funnel analyzer and retention decay power-law curve modeling.

```bash
# Run data pipeline
python src/data_pipeline.py

# Run P&L and unit economics model
python src/pnl_unit_economics.py

# Run retention funnel diagnostics
python src/funnel_retention_analysis.py
```

---

## Product & Growth Strategy Documentation (`docs/`)

To extend the data analytics findings into executive business recommendations, I authored three strategic guides:

1. **[`docs/Mobile_Game_Growth_Strategy.md`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/docs/Mobile_Game_Growth_Strategy.md)**: Strategic playbook for scaling game revenue, hybrid monetization, and P&L margin expansion.
2. **[`docs/Product_Management_PRD.md`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/docs/Product_Management_PRD.md)**: Product Requirement Document featuring VIP Pass, Rewarded Video Boosters, One-Tap Auth, and RICE scoring.
3. **[`docs/Market_Competitor_Analysis.md`](file:///c:/Users/Asus/Downloads/mobile-game-analytics-powerbi-main/docs/Market_Competitor_Analysis.md)**: Competitive market analysis and ad mediation / monetization benchmarking across market tiers.

---

## Tools & Technologies Used

**Data Preparation & Python Analytics**
- Python
- Pandas
- NumPy
- Jupyter Notebook

**Business Intelligence & Visualization**
- Microsoft Power BI
- DAX (Data Analysis Expressions)

**Data Sources**
- Firebase Analytics
- GameAnalytics
- Google AdMob

---

## Dataset Information

The original raw logs used in this project are anonymized/aggregated to protect project-specific business data.

The project uses four analysis-ready datasets located in the `data/` folder:

- `engagement.csv`
- `player_behaviour.csv`
- `monetization.csv`
- `geography.csv`

The repository includes the complete methodology, Python scripts, dashboard screenshots, Power BI data model, DAX library, strategic documentation, and project report to demonstrate the complete end-to-end analytics workflow.

---

## Author Profile

- **Author**: Aman Yadav  
- **GitHub**: [https://github.com/amanyadav01234](https://github.com/amanyadav01234)  
