import world_creation
from modules import language, player
from pprint import pprint


def play():
    # Create the world:
    world = world_creation.create_world()

    # Initialize iteration variable:
    next_step = True
    _, vocabulary = language.create_vocabulary()

    # pprint(world, depth=3)

    # Describe your starting location:
    player.describe(world['player'], world['player']['location'])

    # Continue steps until the game ends:
    while next_step:
        # Get input from user:
        updates = language.interpret_user_phrase(world['player'], vocabulary)
        next_step = updates['next_step']
        step_type = updates['step_type']
        action = updates['action']

        for reaction in world['player']['reactions'][action]:
            if step_type == 'transit':
                world['player'] = reaction(world['player'], updates['direction'])

            elif step_type == 'item_interaction':
                world['player'] = reaction(world['player'], world['items'][updates['item']])

            elif step_type == 'object_interaction':
                world['player'] = reaction(world['player'], world['objects'][updates['object']])

    print('Game Over!')


if __name__ == '__main__':
    play()
