import pandas as pd

from prophet import Prophet


class FinancialForecaster:

    @staticmethod
    def forecast_expenses(df: pd.DataFrame):

        # Use only expenses
        expense_df = df[
            df["transaction_type"] == "Expense"
        ].copy()

        # Prepare Prophet format
        prophet_df = expense_df[["date", "amount"]]

        prophet_df.columns = ["ds", "y"]

        # Prophet expects positive values
        prophet_df["y"] = prophet_df["y"].abs()

        # Group by date
        prophet_df = (
            prophet_df.groupby("ds")["y"]
            .sum()
            .reset_index()
        )

        # Train model
        model = Prophet()

        model.fit(prophet_df)

        # Future dates
        future = model.make_future_dataframe(
            periods=30
        )

        forecast = model.predict(future)

        # Return important forecast columns
        return forecast[
            ["ds", "yhat", "yhat_lower", "yhat_upper"]
        ].tail(30).to_dict(orient="records")