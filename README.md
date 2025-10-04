# Log Analytics Pipeline 

A real-world Data Engineering project that processes application logs, cleans them, and loads results into SQLite and Elasticsearch for analytics.

## Usage
1. Generate logs: `python src/generator.py`  
2. Run the full pipeline: `python src/main.py`  

## Tech Stack
Python | Pandas | SQLite | Elasticsearch | YAML | Logging

## Project Structure
- `data/raw/` → input log files  
- `data/cleaned/` → cleaned datasets  
- `data/reports/` → SQLite databases and reports  
- `src/` → ETL scripts (extract, transform, load)  
- `config/` → project configuration  
- `logs/` → runtime logs  
- `notebooks/` → Jupyter analysis  

## Author
**Ali Zamanpour** — Data Engineer & AI Specialist
