from gliner import GLiNER

model = GLiNER.from_pretrained("gliner-community/gliner_small-v2.5")

text = """
Cristiano Ronaldo dos Santos Aveiro (born 5 February 1985) is a Portuguese
professional footballer who plays as a forward for and captains both Saudi Pro
League club Al Nassr and the Portugal national team.
"""

labels = ["person", "date", "organization", "location"]

entities = model.predict_entities(text, labels, threshold=0.5)
print(entities)
#for entity in entities:
#    print(entity["text"], "=>", entity["label"])