def is_place(obj: dict):
    """Checks that the passed object is a {place} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'place'


def is_player(obj: dict):
    """Checks that the passed object is a {player} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'player'


def is_item(obj: dict):
    """Checks that the passed object is a {item} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'item'


def is_object(obj: dict):
    """Checks that the passed object is a {object} instance.
    Args:
        obj: Object that should be checked.
    Return:
        True/False
    """
    return obj['category'] == 'object'
