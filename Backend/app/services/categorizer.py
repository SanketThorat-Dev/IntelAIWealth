import pandas as pd


class TransactionCategorizer:

    CATEGORY_KEYWORDS = {
        "Food": ["starbucks", "zomato", "swiggy", "restaurant"],
        "Transport": ["uber", "ola", "rapido"],
        "Shopping": ["amazon", "flipkart", "myntra"],
        "Entertainment": ["netflix", "spotify", "youtube"],
        "Income": ["salary", "bonus", "credited"]
    }

    @staticmethod
    def categorize_transaction(description: str):

        description = str(description).lower()

        for category, keywords in TransactionCategorizer.CATEGORY_KEYWORDS.items():

            for keyword in keywords:

                if keyword in description:
                    return category

        return "Others"

    @staticmethod
    def apply_categories(df: pd.DataFrame) -> pd.DataFrame:

        df["category"] = df["description"].apply(
            TransactionCategorizer.categorize_transaction
        )

        return df