# load_raw_data.py
import json
from pathlib import Path

def load_jsonl(path):
    data = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line)["text"])
    return data

RAW_DIR = Path("dataset/raw")

texts = []
for file in RAW_DIR.glob("*.jsonl"):
    texts.extend(load_jsonl(file))

print("Total texts:", len(texts))