def run_interpreter():
    # Initialize array to store values:
    arr, i, pointer = initializer()

    # Get algorithm from user
    alg = get_alg()

    # Check that there is no error in the algorithm:
    if check_alg(alg):

        # Parse the algorithm:
        parse_alg(arr, i, alg, pointer)

    else:
        print('Your algorithm has missing parenthesis, check it and than try again')


def initializer():
    """ Create initial parameters.

    :return: arr, i, alg, pointer
    """
    arr = [0]  # Initial array to store values
    i = 0  # Array pointer
    pointer = 0  # Algorithm pointer
    return arr, i, pointer


def get_alg():
    '''
    Receives string from user and clean it from unknown orders
    '''
    command_list = ['<', '>', '+', '-', '[', ']', '.', ',']  # List of acceptible orders
    # alg = input('Please enter your algorithm: ')  # Get input from user
    alg = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'

    # Iterate over each symbol in user input and leave only acceptable ones:
    alg = ''.join([letter for letter in alg.strip() if letter in command_list])

    return alg


def check_alg(alg):
    return alg.count('[') == alg.count(']')


def parse_alg(arr, i, alg, pointer):
    # Iterate over algorithm according to its orders:
    while pointer < len(alg):
        arr, i, pointer = execute(arr, i, alg, pointer)


def execute(arr, i, alg, pointer):
    """ Execure single order from the algorithm """

    # Get the current command:
    order = alg[pointer]

    ####################### Order Selector #######################

    if order == '>':  # > : Move forward:
        return move_forward(arr, i, alg, pointer)

    elif order == '<':  # "<" : Move backward:
        return move_backward(arr, i, alg, pointer)

    elif order == '+':  # "+" : Increase value in the current cell by 1:
        return increase_value(arr, i, alg, pointer)

    elif order == '-':  # "-" : Decrease value in the current cell by 1:
        return decrease_value(arr, i, alg, pointer)

    elif order == '.':  # "." : Convert ASCII code from current cell into symbol and print:
        return print_value(arr, i, alg, pointer)

    elif order == ',':  # "," : Get input form user and save it in the current cell:
        return save_value(arr, i, alg, pointer)

    elif order == '[':  # "[" : Start of cycle:
        return start_cycle(arr, i, alg, pointer)


    elif order == ']':  # "]" : End of cycle:
        return end_cycle(arr, i, alg, pointer)


def move_forward(arr, i, alg, pointer):
    # Check that we didn't reach the end of the array:
    if i == len(arr) - 1:
        # If yes, add another cell to the array:
        arr.append(0)
    # Move array index forward:
    i += 1
    pointer += 1
    return arr, i, pointer


def move_backward(arr, i, alg, pointer):
    if i == 0:
        arr = [0] + arr
    else:
        i -= 1
    pointer += 1
    return arr, i, pointer


def increase_value(arr, i, alg, pointer):
    arr[i] += 1
    pointer += 1
    return arr, i, pointer


def decrease_value(arr, i, alg, pointer):
    arr[i] -= 1
    pointer += 1
    return arr, i, pointer


def print_value(arr, i, alg, pointer):
    print(chr(arr[i]), end='')
    pointer += 1
    return arr, i, pointer


def save_value(arr, i, alg, pointer):
    arr[i] = int(input('Enter your value: '))
    pointer += 1
    return arr, i, pointer


def start_cycle(arr, i, alg, pointer):
    # Check the value in the current array cell:
    if not arr[i]:
        # If value of current cell is '0' then skip the cycle

        par_ind = 1  # Parenthesis index of current cycle

        while par_ind > 0 and pointer < len(alg):
            pointer += 1  # Move forward

            if alg[pointer] == ']':  # Find cycle end
                par_ind -= 1  # Reduce parenthesis index by 1

            elif alg[pointer] == '[':  # Find start of another cycle
                par_ind += 1

    pointer += 1
    return arr, i, pointer


def end_cycle(arr, i, alg, pointer):
    # Check the value in the current array cell:
    if arr[i]:
        # If value of current cell is not '0' then return to the beginning of the cycle:

        par_ind = 1  # Parenthesis index of current cycle

        while par_ind > 0 and pointer < len(alg):
            pointer -= 1  # Move backward

            if alg[pointer] == ']':  # Find end of another cycle
                par_ind += 1  # Reduce parenthesis index by 1

            elif alg[pointer] == '[':  # Find start of cycle
                par_ind -= 1

    pointer += 1
    return arr, i, pointer



run_interpreter()