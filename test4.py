# arrays = [[1, 2, 7], [4, 5, 2], [3, 8, 1], [6, 2, 9]]

# sorted_arrays = sorted(arrays, key=lambda x: x[2], reverse=True)

# print(sorted_arrays)


def replace_empty_with_dash(arr):
    new_arr = []
    for value in arr:
        if value == '':
            new_arr.append('-')
        else:
            new_arr.append(value)
    return new_arr

# Sử dụng hàm để chuyển đổi mảng
# arr = ['1', '', '', '2', '', '', '', '', '', '10', '']
# new_arr = replace_empty_with_dash(arr)
# print(new_arr)