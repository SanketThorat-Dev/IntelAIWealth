import pandas as pd


class FinancialTrends:

    @staticmethod
    def monthly_summary(df: pd.DataFrame):

        # Ensure datetime
        df["date"] = pd.to_datetime(df["date"])

        # Create month column
        df["month"] = df["date"].dt.to_period("M").astype(str)

        # Monthly income
        monthly_income = (
            df[df["transaction_type"] == "Income"]
            .groupby("month")["amount"]
            .sum()
            .to_dict()
        )

        # Monthly expenses
        monthly_expenses = (
            df[df["transaction_type"] == "Expense"]
            .groupby("month")["amount"]
            .sum()
            .abs()
            .to_dict()
        )

        return {
            "monthly_income": monthly_income,
            "monthly_expenses": monthly_expenses
        }
    
    @staticmethod
    def detect_spending_trend(monthly_expenses: dict):

        months = list(monthly_expenses.keys())
        values = list(monthly_expenses.values())

        if len(values) < 2:
            return "Not enough data for trend analysis."

        latest = values[-1]
        previous = values[-2]

        if latest > previous:
            growth = ((latest - previous) / previous) * 100

            return f"Expenses increased by {growth:.2f}% compared to previous month."

        elif latest < previous:
            decline = ((previous - latest) / previous) * 100

            return f"Expenses decreased by {decline:.2f}% compared to previous month."

        return "Expenses remained stable."
    
    @staticmethod
    def detect_recurring_transactions(df: pd.DataFrame):

        recurring = (
            df.groupby("description")
            .size()
            .reset_index(name="count")
        )

        recurring = recurring[recurring["count"] > 1]

        return recurring.to_dict(orient="records")