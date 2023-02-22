# isHot = True
# isCold = True
# if isHot:
#     print("It's a hot day")
#     print("Wear some light clothes")
# elif isCold:
#     print("It's a cold day")
#     print("Put on a jacket")
# else:
#     print("It's a lovely day")
# print('Enjoy your day')

price = 1000000
hasGoodCredit = True
if hasGoodCredit:
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
message = f'Down payment: ${downPayment}'
print(message)