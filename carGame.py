command = ''
isCarOn = False
while command.lower() != 'quit':
    command = input(">")
    if command.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command.lower() == 'start':
        if not isCarOn:
            isCarOn = True
            print('Car started...Ready to go!')
        else:
            print('Car is already started!')
    elif command.lower() == 'stop':
        if isCarOn:
            isCarOn = False
            print('Car stopped.')
        else:
            print('Car has not been started!')
    elif command.lower() == 'quit':
        exit()
    else:
        print("I don't understand that...")
        print('Type in "help" for commands.')