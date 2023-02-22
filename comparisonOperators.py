# temp = 30

# if temp > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

name = input('Type name: ')
if len(name) < 3:
    print("Name is too short!")
elif len(name) >= 50:
    print('Name is too long!')
else:
    print("Name looks good!")