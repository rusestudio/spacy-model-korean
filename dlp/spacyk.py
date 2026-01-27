from kiwipiepy import Kiwi
import spacy

nlp = spacy.load("ko_core_news_lg") #todo later add custom spacy model
kiwi = Kiwi()

def kiwip(text: str) -> str:
    tokens = kiwi.tokenize(text)
    return " ".join(t.form for t in tokens)

#SENSITIVE_KEYWORD = ["API"]
#add more label and ner label

#extract entity target
def get_ner(text):
    clean_text = kiwip(text)
    doc = nlp(clean_text)

    results = []
    for ent in doc.ents:
        if ent.label_ in {"PS", "OG", "MONEY", "CARDINAL", "QUANTITY", "PERCENT"}:
            results.append({
                "type": "NER",
                "label": ent.label_,
                "value": ent.text
            })

    return results