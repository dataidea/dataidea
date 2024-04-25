# Car program

# Get user input
print(
        'Commands: \n'
        '----------- \n'
        '> start \n'
        '> stop \n'
        '> exit \n'
        )

previous_command = ''

while True:
    current_command = input('Enter command here: ')

    if current_command == 'start':
        if previous_command == 'start':
            print('The car is already moving...')
        else:
            print('Starting the car...')
            previous_command = 'start'
    
    elif current_command == 'stop':
        if previous_command == 'stop':
            print('The car has already stopped.')
        else:
            print('Stopping the car...')
            previous_command = 'stop'

    elif current_command == 'exit':
        if previous_command == 'stop':
            break
        else:
            print('You need to stop the car first.')
    else:
        print('Invalid command')


