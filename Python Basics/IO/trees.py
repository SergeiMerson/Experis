with open(r'd:\Projects\ExperisAcademy\Exercises\IO\redwood-data.txt', 'r') as input_file:
    next(input_file)
    next(input_file)
    tree_data = []
    current_ind = highest_ind = highest_height = biggest_ind = biggest_diameter = 0
    for line in input_file:
        cols = [col.strip() for col in line.split('\t')]
        tree_name, tree_place, tree_diameter, tree_height = cols[0], cols[1], float(cols[2]), float(cols[3])

        tree_data.append([tree_name, tree_place, tree_diameter, tree_height])
        if tree_height > highest_height:
            highest_height = tree_height
            highest_ind = current_ind

        if tree_diameter > biggest_diameter:
            biggest_diameter = tree_diameter
            biggest_ind = current_ind

        current_ind += 1

print(f'The biggest tree is {tree_data[biggest_ind][0]} with a diameter of {tree_data[biggest_ind][2]}')
print(f'The highest tree is {tree_data[highest_ind][0]} with a height of {tree_data[highest_ind][3]}')

