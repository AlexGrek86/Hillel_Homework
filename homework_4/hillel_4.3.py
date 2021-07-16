import re

some_text = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro        "
result = re.findall(r"(\w+)=([^\s&]+)", some_text)

final_dictionary = {x: y for x, y in result}

print(final_dictionary)
