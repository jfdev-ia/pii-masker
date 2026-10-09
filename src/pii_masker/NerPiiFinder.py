from gliner2 import GLiNER2

model = GLiNER2.from_pretrained("fastino/gliner2-privacy-filter-PII-multi")

def find_pii_entities(text):
    pii_labels = [
    "person", "date of birth", "social security number", "email", "gender", "location",
    "phone number", "insurance id", "address", "identitification", "id code", "key code", "handle code",
    "family name"
    ]
    return model.extract_entities(
        text,
        pii_labels,
        threshold=0.5,
        include_confidence=True,
        include_spans=True,
    )