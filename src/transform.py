import os, pandas as pd
from datetime import datetime

def clean_logs(logs, output_dir="data/cleaned"):
    if not logs:
        print("️ No logs to clean.")
        return None

    df = pd.DataFrame(logs)
    df.drop_duplicates(inplace=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["level"] = df["level"].str.upper()
    df = df.sort_values("timestamp")
    df = df[df["level"].isin(["INFO", "WARNING", "ERROR"])]

    os.makedirs(output_dir, exist_ok=True)
    file = os.path.join(output_dir, f"cleaned_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    df.to_csv(file, index=False, encoding="utf-8")
    print(f" Cleaned {len(df)} logs saved → {file}")
    return file
