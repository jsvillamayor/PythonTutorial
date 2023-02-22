highIncome = False
goodCredit = False
if (highIncome and goodCredit) or (not highIncome and not goodCredit):
    print('Eligible for loan')
else:
    print('Not eligible for loan')