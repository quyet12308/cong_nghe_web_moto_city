arrays = [[1, 2, 7], [4, 5, 2], [3, 8, 1], [6, 2, 9]]

sorted_arrays = sorted(arrays, key=lambda x: x[2], reverse=True)

print(sorted_arrays)