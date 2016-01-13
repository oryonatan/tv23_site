import json

with open("primo.json", encoding='utf-8') as f:
    d = json.load(f)

with open("primo-nice.json", "w", encoding='utf-8') as f:
    d = json.dump(d, f, indent=2)


print("Done.")