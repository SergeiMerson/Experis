import language as lng


def add_reaction(obj: dict, action: str, reaction, args: tuple = ()):
    # Check that keyword is in command list:
    if not lng.check_command(action):
        print('Such action is not available')
    else:
        obj['reactions'][action] = obj['reactions'].get(action, [])
        obj['reactions'][action].append((reaction, args))


def remove_reaction(obj: dict, action: str, reaction_ind=-1, remove_all=False):
    if remove_all:
        try:
            del obj['reactions'][action]
        except KeyError:
            print('There is no reactions for such action')
    else:
        try:
            obj['reactions'][action].pop(reaction_ind)
        except KeyError:
            print('There is no such reaction index')


def replace_reaction(obj: dict, action: str, reaction_ind, reaction_new, args: tuple = ()):
    try:
        obj['reactions'][action][reaction_ind] = (reaction_new, args)
    except KeyError:
        print('There is no such reaction number')


def print_reactions(obj: dict, action: str):
    try:
        # Print list of existing functions:
        for i, reaction in enumerate(obj['reactions'][action]):
            print('Reaction #{}: {}'.format(i, reaction))
    except KeyError:
        print('There is no reactions for such action')


def apply_actions(obj: dict, action: str):
    try:
        for reaction in obj['reactions'][action]:
            func = reaction[0]
            args = reaction[1]
            if len(args) == 0:
                func()
            else:
                func(*args)
    except KeyError:
        print('There is no reaction for such action')
