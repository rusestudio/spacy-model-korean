#build docbin 
# build_docbin.py
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
from auto_label import find_entities
from load_raw_data import texts

nlp = spacy.blank("ko")   # PURE spaCy, no MeCab, label
nlp.tokenizer = spacy.tokenizer.Tokenizer(nlp.vocab)
db = DocBin()

error_log = open("dataset/processed/err_spans.txt", "w", encoding="utf-8")

for text in tqdm(texts):
    doc = nlp.make_doc(text)
    ents = []
    used_tokens = set()

    for start, end, label in find_entities(text):
        span = doc.char_span(start, end, label=label, alignment_mode="strict")
        if span is None:
            error_log.write(f"{text} | {start}:{end}\n")
            continue

        # prevent overlapping entities
        token_ids = set(range(span.start, span.end))
        if used_tokens & token_ids:
            continue

        used_tokens |= token_ids
        ents.append(span)

    doc.ents = ents
    db.add(doc)

error_log.close()

db.to_disk("dataset/spacy/all.spacy")
print("Saved DocBin")