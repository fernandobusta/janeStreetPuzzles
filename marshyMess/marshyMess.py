#!/usr/bin/env python3

from forest import Field

def main():

	# Open the file with the forest
	with open("forest.txt") as f:
		forest = [[], [], [], []]
		counter = 0
		# For every line in txt -> store as one element of array
		for span in f:
			if span == '\n':
				counter += 1
			else:
				# This is one line, or a span in the field
				sp = [int(x) for x in span if (x != ' ' and x != '\n')]
				# Append span to field (Array of spans)
				forest[counter].append(sp)

	# Create field objects
	first = Field(forest[0])
	second = Field(forest[1])
	third = Field(forest[2])
	fourth = Field(forest[3])
	#print(first.get_columns())
	print(first)
	print('\n') 
	print(second)
	print('\n')
	print(third)
	print('\n')
	print(fourth)



if __name__ == "__main__":
	main()
