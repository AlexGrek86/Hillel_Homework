bigno_blacklist = {'Adam Miller', 'Bruno Smith', 'Calvin Brown'}
poker_blacklist = {'Dan Wilson', 'Edgar Taylor', 'Adam Miller'}
majong_blacklist = {'Edgar Taylor', 'Adam Miller', 'Calvin Brown'}

c = bigno_blacklist.intersection(poker_blacklist.intersection(majong_blacklist))

print(c)
