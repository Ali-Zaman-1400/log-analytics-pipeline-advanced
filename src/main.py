import os, logging, yaml
from extract import load_raw_logs
from transform import clean_logs
from load import load_to_sqlite, load_to_elasticsearch

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/pipeline.log", level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

def load_config():
    with open("config/settings.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run_pipeline():
    logging.info(" Starting pipeline...")
    cfg = load_config()
    try:
        logs = load_raw_logs(cfg["data_paths"]["raw"])
        if not logs: return
        cleaned = clean_logs(logs, cfg["data_paths"]["cleaned"])
        if not cleaned: return
        load_to_sqlite(cleaned, db_path=os.path.join(cfg["data_paths"]["reports"], "logs.db"))
        load_to_elasticsearch(cleaned, cfg["elasticsearch"]["index_name"], cfg["elasticsearch"]["host"])
        logging.info(" Pipeline completed successfully.")
        print(" Pipeline completed successfully!")
    except Exception as e:
        logging.exception(e)
        print("️ Pipeline failed. Check logs.")

if __name__ == "__main__":
    run_pipeline()
