import os
import re

# Print current location.
current_location = os.getcwd()
print(current_location)

# Print name of current level.
current_level = os.path.basename(__file__)[0:-3]
print(current_level)

input_files_location = current_location + "\\" + current_level + "\\" + current_level
input_files_paths = [
    input_files_location + "\\" + input_file_name
    for input_file_name in os.listdir(input_files_location)
]
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
        line_as_int = [int(i) for i in re.findall("[0-9]+", line_as_string)]
        lines_without_first.append(line_as_int)
        # print("line " + str(index) + ":", line_as_int)
    return number_on_first_line, lines_without_first


current_input_file_path = input_files_paths[3]
print("current_input_file_path:", current_input_file_path)
number_on_first_line, lines_of_file = read_input_file(current_input_file_path)
# print(lines_of_file[0])
sums = []
for line_index in range(0, len(lines_of_file)):
    # print(sum(line))
    if line_index == len(lines_of_file) - 1:
        sums.append(str(sum(lines_of_file[line_index])))
    else:
        sums.append(str(sum(lines_of_file[line_index])) + "\n")

# f = open("level1_1_small.out", "w")
f = open("level1_2_large.out", "w")
f.writelines(sums)
f.close()
