# auto_label.py
import re
from stock_dict import STOCK_TICKERS

def find_entities(text):
    entities = []

    for ticker in STOCK_TICKERS:
        for match in re.finditer(re.escape(ticker), text):
            start, end = match.start(), match.end()

            # boundary check
            before = text[start-1] if start > 0 else " "
            after = text[end] if end < len(text) else " "

            if before.isalnum() or after.isalnum():
                continue

            entities.append((start, end, "TICKER"))

    return entities