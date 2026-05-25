import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="IntelAIWealth",
    layout="wide"
)

st.title("IntelAIWealth")
st.subheader("AI-Powered Financial Intelligence Platform")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload Bank Statement CSV",
    type=["csv"]
)

if uploaded_file:

    # Send file to backend API
    files = {
        "file": uploaded_file.getvalue()
    }

    response = requests.post(
        f"{os.getenv('BACKEND_URL')}/upload-csv",
        files={
            "file": uploaded_file
        }
    )

    data = response.json()

    # Metrics
    analytics = data["analytics"]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Income",
        f"₹{analytics['total_income']}"
    )

    col2.metric(
        "Total Expenses",
        f"₹{analytics['total_expenses']}"
    )

    col3.metric(
        "Net Savings",
        f"₹{analytics['net_savings']}"
    )

    st.divider()

    # Insights
    st.subheader("Financial Insights")

    for insight in data["insights"]:
        st.success(insight)

    st.divider()

    # Category Spending Chart
    st.subheader("Category-wise Spending")

    category_data = analytics["category_spending"]

    category_df = pd.DataFrame({
        "Category": category_data.keys(),
        "Amount": category_data.values()
    })

    fig = px.pie(
        category_df,
        names="Category",
        values="Amount",
        title="Expense Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Monthly Trends
    st.subheader("Monthly Expense Trends")

    monthly_expenses = data["monthly_trends"]["monthly_expenses"]

    trend_df = pd.DataFrame({
        "Month": monthly_expenses.keys(),
        "Expenses": monthly_expenses.values()
    })

    trend_fig = px.line(
        trend_df,
        x="Month",
        y="Expenses",
        markers=True,
        title="Monthly Expenses"
    )

    st.plotly_chart(trend_fig, use_container_width=True)

    st.divider()

    # Anomalies
    st.subheader("Detected Financial Anomalies")

    anomalies = data["anomalies"]

    if anomalies:

        anomaly_df = pd.DataFrame(anomalies)

        st.dataframe(anomaly_df)

    else:
        st.success("No anomalies detected.")

    #Expense Forecast
    st.divider()

    st.subheader("30-Day Expense Forecast")

    forecast_df = pd.DataFrame(data["forecast"])

    forecast_fig = px.line(
        forecast_df,
        x="ds",
        y="yhat",
        labels={'ds': 'Date', 'yhat': 'Predicted Value'},
        title="Predicted Future Expenses"
    )

    st.plotly_chart(
        forecast_fig,
        use_container_width=True
    )

    #AI Coach
    st.divider()

    st.subheader("AI Financial Coach")

    st.info(data["ai_coaching"])

    #Budget Agent
    st.divider()

    st.subheader("Autonomous Budget Planning Agent")

    st.success(
        data["agent_recommendation"]
    )