from fastapi import APIRouter, UploadFile, File
import pandas as pd

from Backend.app.services.normalizer import TransactionNormalizer
from Backend.app.services.categorizer import TransactionCategorizer
from Backend.app.services.analytics import FinancialAnalytics
from Backend.app.services.insights import FinancialInsights
from Backend.app.services.trends import FinancialTrends  
from Backend.app.ml.anomaly_detector import FinancialAnomalyDetector
from Backend.app.ml.forecasting import FinancialForecaster

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        return {
            "error": "Only CSV files are supported"
        }

    # Read CSV
    df = pd.read_csv(file.file)

    # Normalize transactions
    normalized_df = TransactionNormalizer.normalize(df)

    # Apply intelligent categorization
    normalized_df = TransactionCategorizer.apply_categories(normalized_df)

    #Provides Analytics of the transactions
    analytics = FinancialAnalytics.calculate_summary(normalized_df)

    #Provides Financial Insights
    insights = FinancialInsights.generate_insights(analytics)

    #Provides Trend Analytics
    monthly_data = FinancialTrends.monthly_summary(normalized_df)

    #Generates Anomalies
    anomalies = FinancialAnomalyDetector.detect_anomalies(
    normalized_df)

    spending_trend = FinancialTrends.detect_spending_trend(
        monthly_data["monthly_expenses"]
    )

    recurring_transactions = FinancialTrends.detect_recurring_transactions(
        normalized_df
    )

    #Generates Forecast
    forecast = FinancialForecaster.forecast_expenses(
    normalized_df)

    return {
    "filename": file.filename,
    "columns": list(normalized_df.columns),
    "rows": len(normalized_df),
    "analytics": analytics,
    "insights": insights,
    "monthly_trends": monthly_data,
    "spending_trend": spending_trend,
    "recurring_transactions": recurring_transactions,
    "anomalies": anomalies,
    "forecast": forecast,
    "preview": normalized_df.head().to_dict(orient="records")
    }