from modules import general


def create_place(name: str, description: str):
    """Create a new {place} object.
    Args:
        name: The name of the place to display in the game and to address in functions;
        description: Short description that would be displayed when player gets to the place.
    Return:
        {place} dictionary
    """
    place = {'category': 'place',
             'name': name,
             'description': description,
             'connections': {},
             'items': [],
             'objects': []}

    # Print info message:
    print(f'Successfully created place: {name}')

    return place


def get_dir_options(dir_options: dict = None):
    """Iterate over passed dict and return dist with attached reversed directions.
    Args:
        dir_options: Optional. Dict with one-way directions. If nothing is passed, uses {'South', 'North','East','West'}
    Returns:
        {directions} dictionary
    """
    if dir_options is None:
        dir_options = {'south': 'north', 'east': 'west'}

    directions = dir_options.copy()

    # Iterate over the passed dict and copy reversed directions into the result dict:
    for start, end in dir_options.items():
        directions[end] = start

    # Print info message:
    print(f'Directions were successfully created. Possible options are:')
    for start, end in directions.items():
        print(f'\t{start:>20} <---> {end:<20}')

    return directions


def connect_places(start: dict, end: dict, direction: str, dir_options: dict):
    """ Connect two places to each other. Simultaneously add opposite directions to both places.
    Args:
        start: go from {place}
        end: go to {place}
        direction: "direction"
        dir_options: dict with corresponding directions
    Returns:
        {p1}, {p2} place dictionaries with updated directions
    """
    # Check that both start and end are {place} objects:
    if not (general.is_place(start) and general.is_place(end)):
        print('Error:',
              f'\n\t{start["name"]} is', 'not' * general.is_place(start), 'a place',
              f'\n\t{end["name"]} is', 'not' * general.is_place(end), 'a place')

    # Create connection only if the direction is valid:
    elif direction not in dir_options:
        print(f'There is no such direction as {direction}')

    # Check that start has no previous connection in that direction:
    elif start['connections'].get(direction, False):

        # If there is existing connection, print message and do not change it:
        print(f'{start["name"]} is already connected in {direction} to {start["connections"].get(direction)["name"]}')

    # Check that end has no previous connection in opposite direction:
    elif end['connections'].get(dir_options[direction], False):

        # If there is existing connection, print message and do not change it:
        print("{0} is already connected in opposite direction to {1}"
              .format(end['name'], end['connections'].get(dir_options[direction])['name']))

    else:
        # Create connection for both objects:
        start['connections'][direction] = end
        end['connections'][dir_options[direction]] = start

        # Print info message:
        print(f'Successfully created route: {start["name"]:>20} <---> {end["name"]:<20}')

    return start, end


def remove_connection(p1: dict, direction: str):
    """Removes connection to specified direction from both {start place} and {target place}.
    Args:
        p1: go from {place}
        direction: "direction"
    """
    # Get direction options:
    dir_options = get_dir_options()

    # Check that start has connection in specified direction:
    if p1['connections'].get(direction, False):

        # Save end name for info message:
        p2_name = p1['connections'][direction]['name']
        # Remove connections in both directions:
        del p1['connections'][direction]['connections'][dir_options[direction]]
        del p1['connections'][direction]

        # Print info message:
        print(f'Successfully deleted route: {p1["name"]:>20} <---> {p2_name:<20}')

    else:
        print(f'{p1["name"]} has no connection on {direction}')
