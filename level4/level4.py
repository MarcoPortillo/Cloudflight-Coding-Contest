import os
import re

# Print current location.
current_location = os.getcwd()
print(current_location)

# Print name of current level.
current_level = os.path.basename(__file__)[0:-3]
print("NOW AT LEVEL " + current_level[-1])

input_files_location = current_location + "\\" + current_level + "\\" + current_level
input_files_paths = [
    input_files_location + "\\" + input_file_name
    for input_file_name in os.listdir(input_files_location)
    if ".in" in input_file_name
]

# Display names of input files.
print("INPUT FILES PATHS:")
for input_files_path in input_files_paths:
    print(input_files_path)


def read_input_file(input_file_path):
    with open(input_file_path) as file:
        input_file_lines = file.readlines()

    number_on_first_line = int(input_file_lines[0][0:-1])
    lines_without_first = []
    for index in range(1, len(input_file_lines)):
        line_as_string = input_file_lines[index]
        line_as_int = [int(i) for i in re.findall("-?\d+", line_as_string)]
        lines_without_first.append(line_as_int)
        # print("line " + str(index) + ":", line_as_int)
    return number_on_first_line, lines_without_first


current_input_file_path = input_files_paths[2]
print("NOW PROCESSING FILE " + current_input_file_path + "...")
number_on_first_line, lines_of_file = read_input_file(current_input_file_path)


###################### ACTUAL SOLUTION FOR THIS LEVEL ######################


def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def time_calc(x):
    if x == 0:
        return 1
    else:
        return abs(x)


def calculate_time(line):
    total_time = 0
    for step in line:
        total_time = total_time + time_calc(step)
    return total_time


def get_next_number(current):
    if current > 0:
        possible_numbers = [5, 4, 3, 2, 1]
    else:
        possible_numbers = [-5, -4, -3, -2, -1]
    index = possible_numbers.index(current)
    if index < len(possible_numbers) - 1:
        return possible_numbers[index + 1]
    else:
        return possible_numbers[index]


def generate_movement_sequence(required_sequence_length):
    if required_sequence_length == 0:
        return [0, 0]
    if required_sequence_length == 1:
        return [0, 5, 0]
    if required_sequence_length == -1:
        return [0, -5, 0]
    required_half_length = abs(required_sequence_length) // 2
    first_half_sequence = []
    if required_sequence_length > 0:
        start_number = 5
    else:
        start_number = -5
    while len(first_half_sequence) < required_half_length:
        if first_half_sequence == []:
            next_number = start_number
        else:
            next_number = get_next_number(current_number)
        first_half_sequence.append(next_number)
        current_number = next_number
    print("first_half_sequence:", first_half_sequence)
    second_half_sequence = first_half_sequence[::-1]

    full_sequence = first_half_sequence + second_half_sequence

    if abs(required_sequence_length) % 2 == 1:
        full_sequence.insert(
            len(first_half_sequence),
            get_next_number(first_half_sequence[-1]),
        )

    full_sequence = [0] + full_sequence + [0]
    return full_sequence


movement_sequences = []
for line_index in range(0, number_on_first_line):
    line = lines_of_file[line_index]
    space_station_position_x = line[0]
    space_station_position_y = line[1]
    time_limit = line[2]
    print("NOW AT LINES", line)
    movement_sequence_x = generate_movement_sequence(space_station_position_x)
    movement_sequence_y = generate_movement_sequence(space_station_position_y)

    print("FOR X, WE GOT", movement_sequence_x)
    print("FOR Y, WE GOT", movement_sequence_y)
    print(
        "TOTAL TIME:",
        calculate_time(movement_sequence_x) + calculate_time(movement_sequence_y),
    )

    movement_sequences.append(" ".join([str(i) for i in movement_sequence_x]) + "\n")
    if line_index == len(lines_of_file) - 1:
        movement_sequences.append(" ".join([str(i) for i in movement_sequence_y]))
    else:
        movement_sequences.append(
            " ".join([str(i) for i in movement_sequence_y]) + "\n\n"
        )

for movement_sequence in movement_sequences:
    print(movement_sequence)
    # signs = [sgn(x) for x in line]
    # units_of_space = sum(signs)
    # units_of_time = sum([time_calc(x) for x in line])
    # if line_index == len(lines_of_file) - 1:
    #    pos_time.append(str(units_of_space) + " " + str(units_of_time))
    # else:
    #    pos_time.append(str(units_of_space) + " " + str(units_of_time) + "\n")


# f = open("level4_0_example.out", "w")
# f = open("level4_1_small.out", "w")
f = open("level4_2_large.out", "w")
f.writelines(movement_sequences)
f.close()
