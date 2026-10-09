from PDFTextExtractor import extract_text
from NerPiiFinder import find_pii_entities

pdfFile = "cvs/CV_04.pdf"

def redact_pii_info(text, spans):
    redacted = text
    
    for start, end, label in spans:
        redacted = redacted[:start] + f"[{label.upper()}]" + redacted[end:]
    return redacted

def get_spans_from_entities(result):
    entities = result.get("entities", {})
    spans = []
    for label, values in entities.items():
        for value in values:
            start = value['start']
            if start != -1:
                spans.append((start, start + len(value['text']), label))
    spans.sort(key=lambda s: s[0], reverse=True)
    return spans



raw_text = extract_text(pdfFile)

pii_entities = find_pii_entities(raw_text)

spans = get_spans_from_entities(pii_entities)

# NER specialized model: GLiNER2 
redactedText = redact_pii_info(raw_text, spans)

print(spans)