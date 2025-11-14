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


pos_time = []
for line_index in range(0, number_on_first_line):
    line = lines_of_file[line_index]
    signs = [sgn(x) for x in line]
    units_of_space = sum(signs)
    units_of_time = sum([time_calc(x) for x in line])
    if line_index == len(lines_of_file) - 1:
        pos_time.append(str(units_of_space) + " " + str(units_of_time))
    else:
        pos_time.append(str(units_of_space) + " " + str(units_of_time) + "\n")

#
# f = open("level2_0_example.out", "w")
# f = open("level2_1_small.out", "w")
f = open("level2_2_large.out", "w")
f.writelines(pos_time)
f.close()
