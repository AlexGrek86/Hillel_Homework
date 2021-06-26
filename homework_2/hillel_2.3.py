bigno_blacklist = {'Adam Miller', 'Bruno Smith', 'Calvin Brown'}
poker_blacklist = {'Dan Wilson', 'Edgar Taylor', 'Adam Miller'}
majong_blacklist = {'Edgar Taylor', 'Adam Miller', 'Calvin Brown'}

c = bigno_blacklist.intersection(poker_blacklist.intersection(majong_blacklist))

print(c)

# Good. Only one notice create variables with normal names.
# Because it is hard to understand what is 'c'.
