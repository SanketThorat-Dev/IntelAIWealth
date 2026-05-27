import ollama


class InvestmentAgent:

    @staticmethod
    def analyze(
        analytics,
        spending_trend
    ):

        prompt = f"""
You are an AI investment advisory agent.

Analyze the user's financial condition and provide:
- investment readiness assessment
- savings allocation suggestions
- emergency fund observations
- long-term wealth-building recommendations
- risk-aware investment guidance

Financial Analytics:
{analytics}

Spending Trend:
{spending_trend}

Keep the advice:
- practical
- beginner-friendly
- professional
- concise

Do NOT provide illegal or guaranteed financial advice.
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