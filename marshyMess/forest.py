#!/usr/bin/env python3

# Create class for forest
import collections

class Field(object):

	def __init__(self, field):
		self.field = field

	def sum_row(self):
		sum_row = [sum(x) for x in self.field]
		return sum_row

	def sum_column(self):
		mt = self.get_columns()
		sum_col = [sum(x) for x in mt]
		return sum_col

	# Traspose the matrix
	def get_columns(self):
		# Create array -> dimension = len(m[0])
		mt = [[] for i in range(len(self.field[0]))]
		for i in self.field:
			for j in range(len(i)):
				mt[j].append(i[j])
		return mt

	def sum_field(self):
		sum_fd = sum(self.sum_column())
		return sum_fd

	def value_digits(self):
		vdig = {}
		for i in self.field:
			for x, j in enumerate(i):
				if j in vdig:
					vdig[j] += 1
				else:
					vdig[j] = 1

		return collections.OrderedDict(sorted(vdig.items()))

	def calc_span(self):
		total_span = 17 * 13
		span = self.sum_field()
		empty_spaces = self.value_digits()[0]
		return span / (total_span - empty_spaces)


	def __str__(self):
		lines = []
		lines.append("Row sum: {}".format(self.sum_row()))
		lines.append("Column sum: {}".format(self.sum_column()))
		lines.append("Total sum of spans: {}".format(self.sum_field()))
		lines.append("Value per digit: {}".format(self.value_digits()))
		lines.append("calc span: {}".format(self.calc_span()))
		return '\n'.join(lines)


