import ollama


class FinancialCoach:

    @staticmethod
    def generate_financial_advice(
        analytics,
        insights,
        spending_trend,
        anomalies
    ):

        prompt = f"""
You are an expert AI financial advisor.

Analyze the following financial data and provide:
- spending advice
- savings recommendations
- risk observations
- financial health summary
- actionable coaching

Financial Analytics:
{analytics}

Insights:
{insights}

Spending Trend:
{spending_trend}

Detected Anomalies:
{anomalies}

Keep the response:
- concise
- practical
- professional
- personalized
"""

        response = ollama.chat(
            model="phi3:mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]