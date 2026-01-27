from regex import get_regex
from spacyk import get_ner, kiwip 
from io_utils import read_json, write_json #modularization

#mask data
def mask_text(text: str, targets):
    masked_text = text
    # Extract unique values only
    values = {t["value"] for t in targets}
    # Mask longer strings first (prevents partial masking)
    for v in sorted(values, key=len, reverse=True):
        masked_text = masked_text.replace(v, "*" * len(v))

    return masked_text

# test main
if __name__ == "__main__":

    input_data = read_json("input.json")
    text = input_data["text"]

    print("Original text:")
    print(text)
    print("-" * 50)

    regex_targets = get_regex(text)
    ner_targets = get_ner(text) 

    all_targets = regex_targets + ner_targets

    
    masked = mask_text(text, all_targets)
    print("Masked text:")
    print(masked)

    write_json("output/detected.json", all_targets)
    write_json("output/masked.json", {
        "masked_text": masked
    })

    write_json("output/result.json", {
        "original_text": text,
        "masked_text": masked,
        "detected": all_targets
    })

    print("DLP 전처리 완료")


    
