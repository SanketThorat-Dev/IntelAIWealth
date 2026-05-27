import ollama


class RiskAgent:

    @staticmethod
    def analyze(
        analytics,
        anomalies,
        spending_trend
    ):

        prompt = f"""
You are a financial risk analysis AI agent.

Analyze:
- spending behavior
- anomalies
- spending trends

Determine:
- financial risk level
- overspending risk
- stability observations

Analytics:
{analytics}

Anomalies:
{anomalies}

Trend:
{spending_trend}
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