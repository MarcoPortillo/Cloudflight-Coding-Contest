import os

# Print current location.
current_location = os.getcwd()
print(current_location)

# Print name of current level.
current_level = os.path.basename(__file__)[0:-3]
print(current_level)

input_files_location = current_location + "\\" + current_level + "\\" + current_level
input_files = os.listdir(input_files_location)
print("input_files:", input_files)
inputs = {}

for input_file in input_files:
    with open(input_files_location + "\\" + input_file) as file:
        input = file.read()
        inputs[input_file] = input

print(inputs.keys())
print(inputs["level1_0_example.in"])
