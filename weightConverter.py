weightStr = input("Weight: ")
weightTypeStr = input("(L)bs or (K)g: ")
weight = float(weightStr)
if weightTypeStr[0].lower() == 'l':
    message = f'You are {weight * 0.453592} kilos'
elif weightTypeStr[0].lower() == 'k':
    message = f'You are {weight * 2.20462} pounds'
else:
    message = 'Invalid input(s)'
print(message)