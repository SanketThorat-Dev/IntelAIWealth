import pandas as pd


class TransactionNormalizer:

    COLUMN_MAPPINGS = {
        "date": ["date", "transaction_date", "txn_date"],
        "description": ["description", "details", "narration"],
        "amount": ["amount", "transaction_amount", "value"],
        "transaction_type": ["type", "transaction_type", "category"]
    }

    @staticmethod
    def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:

        # Create lowercase column mapping
        lowercase_columns = {
            col.lower(): col for col in df.columns
        }

        renamed_columns = {}

        for standard_col, possible_names in TransactionNormalizer.COLUMN_MAPPINGS.items():

            for name in possible_names:
                if name in lowercase_columns:
                    renamed_columns[lowercase_columns[name]] = standard_col
                    break

        df = df.rename(columns=renamed_columns)

        return df

    @staticmethod
    def clean_amounts(df: pd.DataFrame) -> pd.DataFrame:

        if "amount" in df.columns:
            df["amount"] = (
                df["amount"]
                .astype(str)
                .str.replace(",", "")
                .str.replace("₹", "")
                .astype(float)
            )

        return df

    @staticmethod
    def parse_dates(df: pd.DataFrame) -> pd.DataFrame:

        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

        return df

    @staticmethod
    def normalize(df: pd.DataFrame) -> pd.DataFrame:

        df = TransactionNormalizer.standardize_columns(df)
        df = TransactionNormalizer.clean_amounts(df)
        df = TransactionNormalizer.parse_dates(df)

        return df