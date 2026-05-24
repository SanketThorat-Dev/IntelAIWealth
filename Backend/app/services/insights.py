class FinancialInsights:

    @staticmethod
    def generate_insights(analytics: dict):

        insights = []

        total_income = analytics["total_income"]
        total_expenses = analytics["total_expenses"]
        net_savings = analytics["net_savings"]
        top_category = analytics["top_category"]

        # Savings ratio
        if total_income > 0:

            savings_ratio = (net_savings / total_income) * 100

            if savings_ratio >= 50:
                insights.append(
                    "Excellent savings rate detected."
                )

            elif savings_ratio >= 20:
                insights.append(
                    "Healthy savings pattern observed."
                )

            else:
                insights.append(
                    "Your savings rate is relatively low."
                )

        # Spending category insight
        if top_category:
            insights.append(
                f"Your highest spending category is {top_category}."
            )

        # Expense warning
        if total_expenses > total_income:
            insights.append(
                "Warning: expenses exceed income."
            )

        return insights