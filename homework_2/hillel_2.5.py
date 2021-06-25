guests_vip = {'Adam Miller', 'Bruno Smith', 'Calvin Brown'}
guests_all = {'Edgar Taylor', 'Adam Miller', 'Stive  Morgan',
              'Adam Miller', 'Bruno Smith', 'Calvin Brown',
              'Marta King', 'Eva Kong'}

vip_hall = frozenset(guests_vip)
common_hall = {'Marta King', 'Eva Kong'}
common_hall.update(vip_hall.symmetric_difference(guests_all))

print(vip_hall)
print(common_hall)
