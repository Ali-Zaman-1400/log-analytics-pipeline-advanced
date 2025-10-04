import os, random, json
from datetime import datetime

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]
USERS = ["ali", "sara", "reza", "mina", "admin"]

def generate_log_entry():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(LEVELS),
        "user": random.choice(USERS),
        "message": random.choice([
            "Login successful", "Connection timeout",
            "File not found", "Invalid credentials",
            "Request completed successfully", "Database error"
        ])
    }

def save_logs(num=1000, output_dir="data/raw"):
    os.makedirs(output_dir, exist_ok=True)
    file = os.path.join(output_dir, f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl")
    with open(file, "w", encoding="utf-8") as f:
        for _ in range(num):
            json.dump(generate_log_entry(), f)
            f.write("\n")
    print(f" {num} logs generated → {file}")

if __name__ == "__main__":
    save_logs(1000)
