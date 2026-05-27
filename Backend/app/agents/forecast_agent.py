import ollama


class ForecastAgent:

    @staticmethod
    def analyze(forecast):

        prompt = f"""
You are a financial forecasting AI agent.

Analyze future expense predictions and provide:
- spending trajectory insights
- future risk observations
- financial planning recommendations

Forecast Data:
{forecast}
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