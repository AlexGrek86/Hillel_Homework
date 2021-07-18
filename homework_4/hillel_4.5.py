import re

with open("./text", 'r', encoding='utf-8') as f:
    translation = f.read()
    text = re.split(r'[\.]\s+', translation)

for sentence in text:
    print(sentence)
    print()

# Really good. It is the shortest regular expression for split.
# But as I can see every sentence does not contain dots in the end of sentences
# so that's why it is not perfect.
# -2 points
