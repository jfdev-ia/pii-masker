from PyPDF2 import PdfReader
from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_multi_pii-v1")

reader = PdfReader("cvs/cv5.pdf")
page = reader.pages[0]

text = page.extract_text()
print(text)

# print(text)

labels = ["person", "date", "organization", "location", "job", "gender"]
pii_labels = [
    "person", "date of birth", "social security number", "email", "gender",
    "phone number", "medical facility", "insurance id", "address",
]

entities = model.predict_entities(text, pii_labels, threshold=0.5)

# Redact PII from text
redacted = text
for entity in sorted(entities, key=lambda e: e["start"], reverse=True):
    redacted = redacted[: entity["start"]] + f"[{entity['label'].upper()}]" + redacted[entity["end"] :]

print(redacted)