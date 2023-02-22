# for x in range(4):
#     for y in range(4):
#         print(f'({x}, {y})')
numbers = [5,2,5,2,2]
for item in numbers:
    message = ''
    for x in range(item):
        message += 'x'
    print(message)

