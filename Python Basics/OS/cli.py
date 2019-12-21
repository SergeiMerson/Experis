import execution

exit = False

while not exit:
    user_input = input('Enter your command [or print "exit"]: ').split(' ', maxsplit=1)
    command = user_input[0].lower().strip()
    if len(user_input) > 1:
        arg = user_input[1].lower().strip()

    if command == 'scan':
        try:
            root_name, root_info = execution.scan(arg)
        except NameError:
            print('scan requires argument "path"')
        except TypeError:
            print('Couldn\'t recognize provided path')
    elif command == 'dup':
        try:
            execution.dup(arg, root_info)
        except KeyError:
            print('You need to scan some directory first')
    elif command == 'dirsize':
        try:
            depth = int(arg)
            execution.dirsize(root_info, root_name, depth)
        except KeyError:
            print('You need to scan some directory first')
        except ValueError:
            print('Depth argument should be integer')
    elif command == 'exit':
        exit = True
        print('Have a wonderful day!')
    else:
        print('Couldn\'t interpret your command')
