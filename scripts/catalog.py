import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
items=json.loads((root/'references/catalog.json').read_text())
terms=[s.casefold() for s in sys.argv[1:]]
for item in items:
    hay=(item['name']+' '+item['description']).casefold()
    if not terms or any(t in hay for t in terms):
        print(f"{item['id']} | {item['mode']} | {item['guide']} | {item['description']}")
