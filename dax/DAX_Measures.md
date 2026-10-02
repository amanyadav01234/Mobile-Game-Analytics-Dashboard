# Mobile Game Analytics — Power BI DAX Measures Library

**Author**: Aman Yadav ([github.com/amanyadav01234](https://github.com/amanyadav01234))  

This reference document lists the production DAX measures implemented in the **Mobile Game Analytics Power BI Dashboard** to evaluate player behaviour, retention curves, monetization efficiency, and geographic performance.

---

## 1. Monetization & Revenue Measures

### Total Revenue ($)
```dax
Total Revenue = SUM(Monetization[Total_Revenue_$])
```

### Ad Revenue ($)
```dax
Ad Revenue = SUM(Monetization[Ad_Revenue_$])
```

### In-App Purchase (IAP) Revenue ($)
```dax
IAP Revenue = SUM(Monetization[IAP_Revenue_$])
```

### Ad Revenue Share (%)
```dax
Ad Revenue Share % = 
DIVIDE(
    [Ad Revenue],
    [Total Revenue],
    0
) * 100
```

### Average ARPU ($) — Average Revenue Per User
```dax
Average ARPU = 
DIVIDE(
    [Total Revenue],
    SUM(Monetization[Active_Users]),
    0
)
```

### Average ARPPU ($) — Average Revenue Per Paying User
```dax
Average ARPPU = 
DIVIDE(
    [Total Revenue],
    SUM(Monetization[IAP_Converters]),
    0
)
```

### Average eCPM ($) — Effective Cost Per Mille
```dax
Average eCPM = AVERAGE(Monetization[eCPM_$])
```

---

## 2. Player Engagement & Retention Measures

### DAU / MAU Stickiness Ratio (%)
```dax
DAU / MAU Ratio % = 
AVERAGE(Engagement[DAU_MAU_Ratio_%])
```

### Day-1 Retention Rate (%)
```dax
Day-1 Retention % = AVERAGE(Player_Behaviour[Day_1_Retention_%])
```

### Day-7 Retention Rate (%)
```dax
Day-7 Retention % = AVERAGE(Player_Behaviour[Day_7_Retention_%])
```

### Day-20 Retention Rate (%)
```dax
Day-20 Retention % = AVERAGE(Player_Behaviour[Day_20_Retention_%])
```

### Day-1 Churn Rate (%)
```dax
Day-1 Churn % = 100 - [Day-1 Retention %]
```

### Crash / Technical Error Rate (%)
```dax
Crash Error Rate % = AVERAGE(Player_Behaviour[Crash_Error_Rate_%])
```
