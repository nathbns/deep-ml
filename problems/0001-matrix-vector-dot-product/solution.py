def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

	len_a = len(a[0])
	if len_a != len(b):
		return -1
	
	ans = []
	for vec in a:
		i = 0
		prod = 0
		while i < len_a:
			prod += vec[i] * b[i]
			i += 1
		ans.append(prod)
	return ans