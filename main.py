import json
with open('quotes.json') as f:
  data=json.load(f)
for quote in data['quotes']:
  print(quote['text'])

