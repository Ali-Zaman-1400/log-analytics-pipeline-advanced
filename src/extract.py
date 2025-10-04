import os, json
from glob import glob

def load_raw_logs(raw_dir="data/raw"):
    all_logs = []
    files = sorted(glob(os.path.join(raw_dir, "*.jsonl")))
    if not files:
        print("️ No raw log files found.")
        return all_logs
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    log = json.loads(line.strip())
                    all_logs.append(log)
                except json.JSONDecodeError:
                    print(f"️ Skipping invalid line in {file}")
    print(f" Loaded {len(all_logs)} total logs from {len(files)} files.")
    return all_logs
