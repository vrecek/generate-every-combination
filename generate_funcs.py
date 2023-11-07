from string import ascii_lowercase
from itertools import product



# Get the <arr> arg
def get_arr_arg(arg):
	match arg:
		case 'alpha_low':
				return  list(ascii_lowercase)
		case 'alpha_upp':
				return  list(ascii_lowercase.upper())
		case 'numeric':
				return [str(x) for x in range(0, 10)]
		case _:
			# Verify the custom array
			splitted = arg.split(',')

			if any(len(x) != 1 for x in splitted):
				print_error()

			return splitted



# Generate the combinations
def generate_combinations(ARR, MIN, MAX):
	# Calculate total number of possible combinations	
	total_number_combinations = sum([ len(ARR) ** x for x in range(MIN, MAX + 1) ])
	
	print(f'Total combinations: {total_number_combinations}')
	print('Generating...')

	combinations = []

	# Generate every possible combination
	for currLen in range(MIN, MAX + 1):
		combinations += [ ''.join(x) for x in product(ARR, repeat=currLen) ]

	return combinations



# Prints the error and exists the program
def print_error():
	print('''
	===Usage===:
	python3 generate.py <min> <max> <arr>

	Available <arr>:
	-alpha_low
	-alpha_upp
	-numeric
	-custom

	When specifying a custom array, values must be separated by comma
	h,y,e,b
	1,4,7,8
	r,6,h,8

	### BE AWARE OF THE PERFORMANCE, WHEN SPECIFYING LARGE ARRAYS AND LARGE MIN/MAX VALUES ###
	''')

	exit(1)
