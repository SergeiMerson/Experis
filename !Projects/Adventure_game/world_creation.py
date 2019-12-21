from modules import places, player, objects, interactions, language, general


def create_world():
    # Create dict to store the World objects:
    world = {'player': {}, 'places': {}, 'objects': {}, 'items': {}}

    """ ----------------------------------------------- Create Map ------------------------------------------------ """
    # Create a list of tuples with places and its descriptions:
    place_set = [
        ('Lookout Point', 'The highest point of Monkey Island'),
        ('The Scumm Bar', 'Dirty old bar full of pirates waiting for a next opportunity to get out of this place'),
        ('Kitchen', 'A place more suitable for graveyard that for cooking'),
        ('Circus', 'The sign at the entrance tells "Welcome to the Fettuccini Brother\'s Circus, ' +
         'the only place where you can be really fired"'),
        ('Voodoo Lady\'s Den', 'The strangest place you have ever seen in your life full of different voodoo stuff '),
        ('Victory', 'Congratulation! You win! Just a test location))')
    ]

    # Iterate over this list and add each place to the world dict:
    for location, description in place_set:
        world['places'][location] = places.create_place(name=location, description=description)

    """ ----------------------------------------------- Connect Map ----------------------------------------------- """
    # Get default directions:
    dir_options = places.get_dir_options()

    # Create a list of tuples with places that need to be connected ({start from , {direction to}, {destination}):
    direction_set = [
        ('Lookout Point',       'south',    'The Scumm Bar'),
        ('The Scumm Bar',       'west',     'Kitchen'),
        ('The Scumm Bar',       'east',     'Circus'),
        ('Circus',              'north',    'Voodoo Lady\'s Den'),
        ('Voodoo Lady\'s Den',  'west',     'Lookout Point')
    ]

    # Iterate over this list and connect locations in appropriate direction:
    for start, direction, end in direction_set:
        places.connect_places(
            start=world['places'][start], direction=direction, end=world['places'][end], dir_options=dir_options
        )

    """ ---------------------------------------------- Create Player ---------------------------------------------- """
    # Add a player to the world dict:
    world['player'] = player.create(
        name='Guybrush Threepwood',
        description="I'm Guybrush Threepwood and I want to be a mighty pirate",
        location=world['places']['Lookout Point']
    )

    """ --------------------------------------------- Create Objects ---------------------------------------------- """
    # Create a list of tuples with {objects} names and their descriptions:
    object_set = [
        ('Barrel', 'A wooden barrel full of rotten fish. Uh, tasty ...'),
        ('Table', 'A nicely done expensive table with a plaque telling "Major of Monkey Island". What does it do here?'),
        ('Cannon', 'A rusty cannon for a circus tricks.')
    ]

    # Iterate over this list and add each {object} to the world dict:
    for obj, description in object_set:
        world['objects'][obj] = objects.create_object(name=obj, description=description)

    """ ---------------------------------------------- Place Objects ---------------------------------------------- """
    # Create a list of tuples with {objects} and {places} names:
    object_allocations_set = [
        ('Barrel', 'Kitchen'),
        ('Table', 'The Scumm Bar'),
        ('Cannon', 'Circus')
    ]

    # Iterate over this list and place each {item} to the {place}:
    for obj, place in object_allocations_set:
        objects.put(world['objects'][obj], world['places'][place])

    """ ---------------------------------------------- Create Items ----------------------------------------------- """
    # Create a list of tuples with {items} names and their descriptions:
    item_set = [
        ('Matches', 'A box of matches, made in Monkey Island.'),
        ('Sword', 'Your granddaddy\'s knife that you proudly call "Pirate Slaughter'),
        ('Map', 'An ancient treasure map. It is so ancient that almost no ink left on it'),
        ('Potion',
         'An elixir of Health and Beauty. Why would you ever need it when your are the healthiest handsome man here?')
    ]

    # Iterate over this list and add each place to the world dict:
    for item, description in item_set:
        world['items'][item] = objects.create_item(name=item, description=description)

    """ ------------------------------------------ Place Items to Places ------------------------------------------ """
    # Create a list of tuples with {item} and {target} names:
    item_places_allocations_set = [
        ('Matches', 'The Scumm Bar'),
        ('Potion', 'Kitchen')
    ]

    # Iterate over this list and place each {item} to the {place}:
    for item, place in item_places_allocations_set:
        objects.put(world['items'][item], world['places'][place])

    """ ----------------------------------------- Place Items into Objects ---------------------------------------- """
    # Create a list of tuples with {item} and {target} names:
    item_objects_allocations_set = [
        ('Sword', 'Table'),
        ('Map', 'Barrel')
    ]

    # Iterate over this list and place each {item} to the {place}:
    for item, obj in item_objects_allocations_set:
        objects.put(world['items'][item], world['objects'][obj])

    """ ------------------------------------------- Add Actions to Items ------------------------------------------ """
    # Get a list of default actions and vocabulary:
    commands, vocabulary = language.create_vocabulary()

    # Create a list of tuples of {items} and according {actions}:
    action_set = [
        ('Sword', 'cut'),
        ('Matches', 'burn')
    ]

    # Iterate over this list and assign {action} for each {item}:
    for item, action in action_set:
        interactions.add_action(target=world['items'][item], keyword=action, commands=commands)

    """ ------------------------------------------ Add Abilities to Player ---------------------------------------- """
    # Get a list of default actions and vocabulary:
    commands, vocabulary = language.create_vocabulary()

    # Create a set of basic user {abilities}:
    abilities_set = {'take', 'drop', 'go', 'describe'}

    # Update Player's abilities:
    player.set_abilities(world['player'], abilities_set, commands)

    """ ------------------------------------------ Add Reaction to Player ---------------------------------------- """
    # Get a list of default actions and vocabulary:
    commands, vocabulary = language.create_vocabulary()

    # Create a set of basic user {abilities}:
    user_reactions_set = [
        ('go', player.transit),
        ('describe', player.describe),
        ('take', player.pickup_item),
        ('drop', player.drop_item)
    ]

    # Update Player's reactions:
    for action, reaction in user_reactions_set:
        interactions.add_reaction(target=world['player'], action=action, reaction=reaction, commands=commands)

    return world


world = create_world()
