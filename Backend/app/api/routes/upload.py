from fastapi import APIRouter, UploadFile, File
import pandas as pd

from Backend.app.services.normalizer import TransactionNormalizer
from Backend.app.services.categorizer import TransactionCategorizer
from Backend.app.services.analytics import FinancialAnalytics
from Backend.app.services.insights import FinancialInsights
from Backend.app.services.trends import FinancialTrends  
from Backend.app.ml.anomaly_detector import FinancialAnomalyDetector
from Backend.app.ml.forecasting import FinancialForecaster
from Backend.app.services.llm_coach import FinancialCoach
from Backend.app.agents.budget_agent import budget_agent
from Backend.app.agents.fraud_agent import FraudAgent
from Backend.app.agents.savings_agent import SavingsAgent
from Backend.app.agents.forecast_agent import ForecastAgent
from Backend.app.agents.risk_agent import RiskAgent
from Backend.app.agents.investment_agent import InvestmentAgent

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

    #Generate AI Coaching
    ai_coaching = FinancialCoach.generate_financial_advice(
    analytics=analytics,
    insights=insights,
    spending_trend=spending_trend,
    anomalies=anomalies
    )

    #Budget Agent Workflow
    agent_response = budget_agent.invoke({

    "analytics": analytics,
    "insights": insights,
    "anomalies": anomalies,
    "spending_trend": spending_trend
    })

    #Fraud Agent Workflow
    fraud_analysis = FraudAgent.analyze(anomalies)

    #Savings Agent Workflow
    savings_analysis = SavingsAgent.analyze(
        analytics
    )

    #Forecast Agent Workflow
    forecast_analysis = ForecastAgent.analyze(
        forecast
    )

    #Risk Agent Workflow
    risk_analysis = RiskAgent.analyze(
        analytics,
        anomalies,
        spending_trend
    )

    #Investment agent workflow
    investment_analysis = InvestmentAgent.analyze(
    analytics,
    spending_trend
    )

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
    "ai_coaching": ai_coaching,
    "agent_recommendation": agent_response["recommendation"],
    "fraud_analysis": fraud_analysis,
    "savings_analysis": savings_analysis,
    "forecast_analysis": forecast_analysis,
    "risk_analysis": risk_analysis,
    "investment_analysis": investment_analysis,
    "preview": normalized_df.head().to_dict(orient="records")
    }