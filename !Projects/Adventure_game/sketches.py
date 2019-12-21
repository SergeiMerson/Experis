def go_to_location(player, direction):
    try:
        player['location'] = player['location']['connections'][direction]
    except KeyError:
        print(f'There is nothing on {direction}')

