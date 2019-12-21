from modules import general, language


""" ------------- Creation ------------- """


def create_(name: str, description: str, actions: set = None):
    """Create a new {item} object.
       Items could be placed into Inventory (Player items) and make new actions available to player.
    Args:
        name: The name of the place to display in the game and to address in functions;
        description: Short description that would be displayed when player inspects the item;
        actions: Actions available to this {item}
    Return:
        {item} dictionary
    """
    # Check if action set was provided:
    actions = set() if actions is None else actions

    # Create an item:
    item = {'category': 'item', 'name': name, 'description': description, 'actions': actions, 'location': {}}

    # Print info message:
    print(f'Successfully created item: {name}')

    return item


""" ------------- Placing / moving / removing ------------- """


def put(item: dict, target: dict):
    """Puts {item} object into a {place}.
       Used for pre-play setup or after creation of a new item in the game.
    Args:
        item: The {item} object to be moved to a new place;
        target: Target {place}.
    Return:
        updated {place} and {item} objects
    """
    # Check what is the current item|object location:
    if item.get('location'):  # if there is no location defined for this item, it would return {}, what equals False
        print(f'{item["name"]} is already located in {item["location"]["name"]}, use move() function instead')

    else:
        target['items'].append(item)  # Place the {item} into the {place}
        item['location'] = target     # Update {item} location link

    # Print info message:
    print(f'{item["name"]} was successfully put in {target["name"]}')

    # Return updated values:
    return item, target


def remove(item: dict):
    """Remove {item}/{object} from {place}.
    Args:
        item: The {item}/{object} to be removed;
    Return:
        updated {item} objects
    """
    # Check if the {item}/{object} is placed anywhere:
    if item.get('location'):
        # Save current {item}/{object} location name for info message:
        old_location = item['location']['name']

        # Remove {item}/{object} from its current location:
        item['location']['items'].remove(item)

        # Update the {item}/{object} location:
        del item['location']

        # Print info message:
        print(f'{item["name"]} was successfully removed from {old_location}')

    else:
        print(f'{item["name"]} has no existing location')

    return item


def move(item: dict, new_place: dict):
    """Move item from one {place} to another.
    Args:
        item: The {item} object to be moved to a new place;
        new_place: Target {place} where need to move an item.
    Return:
        updated {place} and {item} objects
    """
    # Remove {item} from current location:
    item = remove(item)

    # put {item} into the target {new_place}:
    new_place['items'].append(item)

    # Update the item/object location:
    item['location'] = new_place

    # Print info message:
    print(f'{item["name"]} was successfully moved to {new_place["name"]}')

    return item, new_place
