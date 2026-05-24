from fastapi import APIRouter, UploadFile, File
import pandas as pd

from Backend.app.services.normalizer import TransactionNormalizer
from Backend.app.services.categorizer import TransactionCategorizer
from Backend.app.services.analytics import FinancialAnalytics
from Backend.app.services.insights import FinancialInsights  

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

    return {
    "filename": file.filename,
    "columns": list(normalized_df.columns),
    "rows": len(normalized_df),
    "analytics": analytics,
    "insights": insights,
    "preview": normalized_df.head().to_dict(orient="records")
    }