def greetUser(fname, lname):
    print(f'Hi {fname} {lname}!')
    print(f'Welcome aboard {fname} {lname}!')

print('Start')
greetUser(lname = 'Villamayor', fname = 'James') 
#arguments can be out of order if you put keyword arguments
#does not have to be in same order as parameters
#use keywords to increase readability
print('Finish')