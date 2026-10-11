import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n, m = len(a[0]), len(a)
	new_n, new_m = new_shape[1], new_shape[0]

	if n*m != new_n*new_m:
		return []

	reshaped_matrix, new_row = [], []
	i, x = 0, 0
	last = []
	for row in a:
		for col in row:
			if x == new_n:
				reshaped_matrix.append(new_row)
				x = 0
				new_row = []
			new_row.append(col)
			last = new_row
			x += 1
	reshaped_matrix.append(last)
	return reshaped_matrix