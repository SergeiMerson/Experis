def print_line(name, size, levels=[], indent=4):
    # Print size:
    nodes = {'I': u'\u2502', 'T': u'\u251c', 'L': u'\u2514'}
    print(f"[{size:>14,.0f}]".center(16), end='')
    # Print lines:
    dir_level = len(levels)
    for i, end_node in enumerate(levels, 1):
        # Check the last level:
        if i == dir_level:
            if not end_node:
                print(f"{nodes['T']:>{indent}s}" + " ", end='')
            else:
                print(f"{nodes['L']:>{indent}s}" + " ", end='')
        # Check other levels:
        else:
            if not end_node:
                print(f"{nodes['I']:>{indent}s}" + " ", end='')
            else:
                print(' ' * indent + " ", end='')
    # Print name:
    print(' ' + name)


def print_subtree(dir_info, levels=[], indent=4, max_depth=False):
    # Get list of subdirectories:
    subdirectories = sorted(dir_info['directories'].keys())
    number_of_subdirectories = len(subdirectories)

    # Print line for each subdirectory:
    for n, dir_name in enumerate(subdirectories, 1):
        end_node = (n == number_of_subdirectories)  # If this is a last dir on this level then True, False otherwise
        current_dir = dir_info['directories'][dir_name]
        dir_size = current_dir['size']
        print_line(dir_name, dir_size, levels + [end_node], indent)

        # Print info for subdirectories:
        if current_dir['directories'] and (len(levels) < max_depth):
            print_subtree(current_dir, levels + [end_node], indent)


def print_tree(root_info, root_name, max_depth=False):
    root_size = root_info['size']

    # Print table head:
    print(f"Directories Tree for [{root_name}]".center(80))
    print('-' * 80, 'Directory Size'.center(16) + 'Directory Name'.center(64), '-' * 80, sep='\n')

    # Print root directory info:
    print_line(root_name, root_size)

    # Print subdirectories info:
    print_subtree(root_info, max_depth=max_depth)
