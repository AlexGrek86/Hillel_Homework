import re

with open("./text", 'r', encoding='utf-8') as f:
    translation = f.read()
    text = re.split(r'[\.]\s+', translation)

    print(text)
