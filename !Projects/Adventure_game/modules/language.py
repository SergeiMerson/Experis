def create_vocabulary(voc: dict = None):
    """Create vocabulary from passed dictionary.
    Args:
        voc: A dictionary of command (as a str): synonyms (as a list)
    Return:
        commands: set with acceptable commands
        inv_voc: inverted dictionary where each synonym added as a key and corresponding command as its value.
    """
    # If no dictionary was passed, create a default one:
    if voc is None:
        voc = {'take': ['get', 'pick'],
               'drop': ['put'],
               'cut': ['slice', 'brake'],
               'go': ['follow', 'run'],
               'use': ['apply'],
               'burn': ['fire'],
               'describe': ['look','check']}

    # Save acceptable commands in a tuple:
    commands = set(voc)

    # Create empty dict to store invented key:value pairs:
    inv_voc = {}

    # Invent original dict and store results in the new one:
    for key, val in voc.items():
        inv_voc = {**inv_voc, **{v: key for v in val}}  # unpacks two dicts and joins them
        inv_voc[key] = key  # if it wasn't specified in synonyms, add command as its own synonym

    return commands, inv_voc


def interpret_user_phrase(player: dict, vocabulary: dict = None):
    """Ask user for input, try to parse it and to get action and subject (could be {item}, {object} or direction)
    Args:
        player: A {player} object;
        vocabulary: A vocabulary of synonyms and corresponding actions.
    Return:
        step_type: transit / item_interaction / object_interaction
        next_step: bool, indicate if to take a next step or to end the Game;
        action: action keyword;
        item: target {item},
        obj: target {object},
        direction: where Player should move;
    """
    # Set initial variable:
    next_step = True
    successful_parse = False
    action = item = obj = direction = step_type = False

    # Fetch  available actions, items, objects and directions:
    av_actions    = player['actions']
    av_items      = {i['name'] for i in player['location']['items']}
    av_objects    = {o['name'] for o in player['location']['objects']}
    av_directions = {d for d in player['location']['connections']}

    # Check if vocabulary was passed, if no, create default one:
    if vocabulary is None:
        _, vocabulary = create_vocabulary()

    # Get input from user until successful parsing:
    while not successful_parse:
        user_input = input('+--> :')

        # Split user input into tokens, make it lowercase and convert it to set:
        user_input = set(user_input.split())

        # Get set interception for each object category:
        # Use vocabulary to find not only commands, but also their synonyms:
        found_actions    = {vocabulary[act] for act in user_input if act in av_actions}
        found_items      = {itm for itm in user_input if itm in av_items}
        found_objects    = {ob for ob in user_input if ob in av_objects}
        found_directions = {drct for drct in user_input if drct in av_directions}

        # If any values where found assign them to variables if there is no ambiguity:
        action    = found_actions.pop()    if len(found_actions) == 1 else False
        item      = found_items.pop()      if len(found_items)   == 1 else False
        obj       = found_objects.pop()    if len(found_objects) == 1 else False
        direction = found_directions.pop() if len(found_directions) == 1 else False

        # Define command type and in case of success set successful_parse as True:
        if action and direction and not (obj or item):
            step_type = 'transit'
            print(f"You went to {direction}")
            successful_parse = True

        elif action and obj and not(item or direction):
            # Check that there is a reaction for passed action in {object}:
            if action in player['location']['objects'][obj]['reactions']:
                step_type = 'object_interaction'
                successful_parse = True
            else:
                print(f"You can't {action} -> {obj}")

        elif action and item and not(obj or direction):
            # Check that there is a reaction for passed action in {object}:
            if action in player['reactions']:
                step_type = 'item_interaction'
                successful_parse = True
            else:
                print(f"You can't {action} -> {item}")
        else:
            print('Your command is slightly ambiguous, try to speak in plain monkish..')
                    
    return {'next_step': next_step,
            'step_type': step_type,
            'action': action,
            'item': item,
            'object': obj,
            'direction': direction}
