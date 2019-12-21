with open(r'd:\Projects\ExperisAcademy\Exercises\IO\ex_19.txt', 'w') as output_file:
    for number in range(1, 1001):
        num_to_add = []
        for power in range(1, 5):
            num_to_add.append(str(number**power))
        print(*num_to_add, sep=', ', file=output_file)


with open(r'd:\Projects\ExperisAcademy\Exercises\IO\ex_19.txt', 'r') as input_file:
    print([line.split(',')[2] for line in input_file.readlines()])