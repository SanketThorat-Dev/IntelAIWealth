import pandas as pd


class FinancialAnalytics:

    @staticmethod
    def calculate_summary(df: pd.DataFrame):

        total_income = df[df["transaction_type"] == "Income"]["amount"].sum()

        total_expenses = abs(
            df[df["transaction_type"] == "Expense"]["amount"].sum()
        )

        net_savings = total_income - total_expenses

        category_spending = (
            df[df["transaction_type"] == "Expense"]
            .groupby("category")["amount"]
            .sum()
            .abs()
            .to_dict()
        )

        top_category = (
            max(category_spending, key=category_spending.get)
            if category_spending
            else None
        )

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_savings": net_savings,
            "category_spending": category_spending,
            "top_category": top_category
        }