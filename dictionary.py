# customer = {
#     'name': 'John Smith',
#     'age' : 30,
#     'isVerified': True
# }
# print(customer.get('birthday', "Jan 1 1998"))

digits = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '0' : 'Zero',
}
message = ''
phone = input('Phone: ')
for item in phone:
    message += digits[item] + ' '
print(message)