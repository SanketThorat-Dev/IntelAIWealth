import pandas as pd

from sklearn.ensemble import IsolationForest


class FinancialAnomalyDetector:

    @staticmethod
    def detect_anomalies(df: pd.DataFrame):

        # Copy dataframe
        anomaly_df = df.copy()

        # Use only numerical feature
        features = anomaly_df[["amount"]]

        # Train Isolation Forest
        model = IsolationForest(
            contamination=0.1,
            random_state=42
        )

        anomaly_df["anomaly"] = model.fit_predict(features)

        # Convert predictions
        anomaly_df["anomaly"] = anomaly_df["anomaly"].apply(
            lambda x: "Anomaly" if x == -1 else "Normal"
        )

        # Filter anomalies
        anomalies = anomaly_df[
            anomaly_df["anomaly"] == "Anomaly"
        ]

        return anomalies.to_dict(orient="records")