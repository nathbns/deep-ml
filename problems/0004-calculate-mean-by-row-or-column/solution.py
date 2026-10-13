def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	ans = []
	if mode == "row":
		for row in matrix:
			sum_row = 0
			for element in row:
				sum_row += element
			ans.append(sum_row / len(row))
	else:
		idx, col = 0, 0
		while idx != len(matrix[0]):
			sum_col = 0
			for row in matrix:
				sum_col += row[idx]
			ans.append(sum_col / len(matrix))
			idx += 1
	
	return ans