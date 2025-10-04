import os, pandas as pd, sqlite3
from elasticsearch import Elasticsearch, helpers

def load_to_sqlite(cleaned_csv, db_path="data/reports/logs.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    df = pd.read_csv(cleaned_csv)
    with sqlite3.connect(db_path) as conn:
        df.to_sql("logs", conn, if_exists="append", index=False)
    print(f" {len(df)} records loaded into SQLite → {db_path}")

def load_to_elasticsearch(cleaned_csv, index_name="system_logs", es_host="http://localhost:9200"):
    df = pd.read_csv(cleaned_csv)
    es = Elasticsearch(es_host)
    if not es.ping():
        print("️ Elasticsearch is not reachable.")
        return
    records = df.to_dict(orient="records")
    actions = [{"_index": index_name, "_source": r} for r in records]
    helpers.bulk(es, actions)
    print(f" {len(records)} records indexed into Elasticsearch → {index_name}")
