from fastapi import APIRouter, UploadFile, File
import pandas as pd

from Backend.app.services.normalizer import TransactionNormalizer

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        return {
            "error": "Only CSV files are supported"
        }

    # Read CSV
    df = pd.read_csv(file.file)

    # Normalize transactions
    normalized_df = TransactionNormalizer.normalize(df)

    return {
        "filename": file.filename,
        "columns": list(normalized_df.columns),
        "rows": len(normalized_df),
        "preview": normalized_df.head().to_dict(orient="records")
    }