"""
Mobile Game Analytics: P&L, Monetization & Unit Economics Optimizer
Author: Aman Yadav (https://github.com/amanyadav01234)

This module models feature P&L, unit economics (LTV vs CAC), ad mediation efficiency,
and net margin optimization scenarios for mobile games.
"""

class MobileGamePnLModel:
    def __init__(self, mau=1000000, dau_mau_ratio=0.22, ad_ecpm=2.50, iap_conv_rate=0.025, 
                 avg_iap_spend=8.50, revshare_pct=0.60, server_cost_per_mau=0.02,
                 cac_per_user=0.45, organic_viral_coefficient=0.35):
        self.mau = mau
        self.dau_mau_ratio = dau_mau_ratio
        self.dau = int(mau * dau_mau_ratio)
        self.ad_ecpm = ad_ecpm
        self.iap_conv_rate = iap_conv_rate
        self.avg_iap_spend = avg_iap_spend
        self.revshare_pct = revshare_pct
        self.server_cost_per_mau = server_cost_per_mau
        self.cac_per_user = cac_per_user
        self.organic_viral_coefficient = organic_viral_coefficient
        
    def calculate_monthly_pnl(self, avg_ad_impressions_per_dau=6.5):
        """Calculates monthly revenue, COGS, gross profit, marketing CAC, and net margin."""
        # 1. Revenue Streams
        monthly_ad_impressions = self.dau * avg_ad_impressions_per_dau * 30
        ad_revenue = (monthly_ad_impressions / 1000.0) * self.ad_ecpm
        
        paying_users = self.mau * self.iap_conv_rate
        iap_revenue = paying_users * self.avg_iap_spend
        gross_platform_revenue = ad_revenue + iap_revenue
        
        # 2. Expense Structure
        publisher_developer_payout = gross_platform_revenue * (1.0 - self.revshare_pct)
        hosting_server_costs = self.mau * self.server_cost_per_mau
        ad_mediation_fee = ad_revenue * 0.05
        payment_gateway_fee = iap_revenue * 0.03
        
        cogs = publisher_developer_payout + hosting_server_costs + ad_mediation_fee + payment_gateway_fee
        gross_profit = gross_platform_revenue - cogs
        gross_margin_pct = (gross_profit / gross_platform_revenue) * 100.0 if gross_platform_revenue > 0 else 0
        
        # 3. Marketing & User Acquisition
        paid_acquisition_ratio = 1.0 / (1.0 + self.organic_viral_coefficient)
        paid_new_users = self.mau * 0.20 * paid_acquisition_ratio
        total_user_acquisition_cost = paid_new_users * self.cac_per_user
        
        net_profit = gross_profit - total_user_acquisition_cost
        net_margin_pct = (net_profit / gross_platform_revenue) * 100.0 if gross_platform_revenue > 0 else 0
        
        # 4. Unit Economics
        arpu = gross_platform_revenue / self.mau
        arppu = gross_platform_revenue / paying_users if paying_users > 0 else 0
        blended_cac = total_user_acquisition_cost / (self.mau * 0.20)
        avg_retention_months = 4.5
        user_ltv = arpu * avg_retention_months
        ltv_cac_ratio = user_ltv / blended_cac if blended_cac > 0 else 0
        
        return {
            "MAU": self.mau,
            "DAU": self.dau,
            "Gross_Revenue_$": round(gross_platform_revenue, 2),
            "Ad_Revenue_$": round(ad_revenue, 2),
            "IAP_Revenue_$": round(iap_revenue, 2),
            "COGS_$": round(cogs, 2),
            "Gross_Profit_$": round(gross_profit, 2),
            "Gross_Margin_%": round(gross_margin_pct, 2),
            "Marketing_CAC_Expense_$": round(total_user_acquisition_cost, 2),
            "Net_Profit_$": round(net_profit, 2),
            "Net_Margin_%": round(net_margin_pct, 2),
            "ARPU_$": round(arpu, 4),
            "ARPPU_$": round(arppu, 2),
            "User_LTV_$": round(user_ltv, 2),
            "Blended_CAC_$": round(blended_cac, 2),
            "LTV_CAC_Ratio": round(ltv_cac_ratio, 2)
        }

    def simulate_growth_trajectory(self):
        """Simulates growth trajectory from baseline to 10x and 100x revenue expansion."""
        scenarios = {
            "Baseline Performance": {"mau": 250000, "ad_ecpm": 2.10, "iap_conv": 0.015, "viral_k": 0.15},
            "Phase 1 Scale": {"mau": 1500000, "ad_ecpm": 3.20, "iap_conv": 0.028, "viral_k": 0.40},
            "Phase 2 Optimization": {"mau": 12000000, "ad_ecpm": 4.80, "iap_conv": 0.045, "viral_k": 0.65}
        }
        
        results = []
        for name, params in scenarios.items():
            model = MobileGamePnLModel(
                mau=params["mau"],
                ad_ecpm=params["ad_ecpm"],
                iap_conv_rate=params["iap_conv"],
                organic_viral_coefficient=params["viral_k"]
            )
            pnl = model.calculate_monthly_pnl()
            pnl["Scenario"] = name
            results.append(pnl)
            
        return results

if __name__ == "__main__":
    print("=== Mobile Game Analytics: P&L & Unit Economics Model ===")
    model = MobileGamePnLModel()
    baseline = model.calculate_monthly_pnl()
    for k, v in baseline.items():
        print(f"  {k}: {v}")
        
    print("\n=== Growth Trajectory Simulation ===")
    growth_data = model.simulate_growth_trajectory()
    for row in growth_data:
        print(f"Scenario: {row['Scenario']:<22} | MAU: {row['MAU']:<10} | Revenue: ${row['Gross_Revenue_$']:<12} | Net Profit: ${row['Net_Profit_$']:<10} | Margin: {row['Net_Margin_%']}%")
