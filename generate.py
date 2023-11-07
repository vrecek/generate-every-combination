from datetime import datetime
from sys import argv
from os import path, mkdir
import generate_funcs as fn


# Handle the args
# Must be exactly 3 args, and the first two must be numbers
if len(argv) < 4 or any(not x.isnumeric() for x in [argv[1], argv[2]]):
	fn.print_error()


# Maximum and minimum length of the combinations
# And verify the <arr> arg
ARR = fn.get_arr_arg(argv[3])
MIN = int(argv[1])
MAX = int(argv[2])


# Check if the filename is specified
try:
	FILENAME = argv[4]

except IndexError:
	FILENAME = 'combinations'


# Create a directory, where the combinations will be stored
if not path.isdir('combinations'):
	mkdir('combinations')


# Starting time
start_time = datetime.now()


# Get and save the combinations
print('Writing...')

combinations = fn.generate_combinations(ARR, MIN, MAX)

with open(f'combinations/{FILENAME}.txt', 'w') as file:
	file.write('\n'.join(combinations))


# Print total execution time
stop_time = datetime.now()
print(f'Execution time: { (stop_time - start_time).total_seconds() } seconds')



