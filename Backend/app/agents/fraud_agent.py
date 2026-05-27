import ollama


class FraudAgent:

    @staticmethod
    def analyze(anomalies):

        prompt = f"""
You are a fraud detection AI agent.

Analyze the following anomalies and determine:
- suspicious transactions
- unusual behavior
- fraud risk observations

Anomalies:
{anomalies}

Provide concise professional analysis.
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