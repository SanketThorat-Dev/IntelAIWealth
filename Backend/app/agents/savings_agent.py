import ollama


class SavingsAgent:

    @staticmethod
    def analyze(analytics):

        prompt = f"""
You are a savings optimization AI agent.

Analyze the user's finances and provide:
- savings improvement strategies
- unnecessary expense observations
- budgeting suggestions

Financial Analytics:
{analytics}
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