import re

some_text = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro        "
result = re.findall(r"(\w+)=([^\s&]+)", some_text)

final_dictionary = {x: y for x, y in result}

print(final_dictionary)

# Really good. Short and effective solution using regular expressions.
# Take a look how it could be implemented with str methods only^
# result = dict()
#
# for pair in some_string.strip().split('&'):
#     if pair:
#         key, value = pair.split('=', maxsplit=1)
#         result[key] = value
#
# print(result)