friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]

for i in friends_list:
    name = "Name"
    print(f"{name.center(10,'*')}")
    print(i.rjust(10))

# Well almost right but not what I expected to see
# ***Name***
#       John
# ***Name***
#      Marta
# ***Name***
#      James
# ***Name***
#     Amanda
# ***Name***
#   Marianna

# Should be
# ***Name***
#       John
#      Marta
#      James
#     Amanda
#   Marianna

# also as I can see you have implemented only solution with rjust.
# should be implemented solution with formatting with fstring too.
# -3 points