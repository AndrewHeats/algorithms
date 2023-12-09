def get_neighbours(current_position, matrix):
    neigh_list = []
    mat_height, mat_width = len(matrix), len(matrix[0])
    height, width = current_position
    if width + 1 < mat_width:
        neigh_list.append((height, width + 1))
    for i in range(mat_height):
        for j in range(mat_width):
            if matrix[i][j] == matrix[height][width] and (i, j) != (height, width) and j > width:
                neigh_list.append((i, j))
    return list(set(neigh_list))


def indiana_jones(matrix: list[list[str]], matrix_height: int, matrix_width: int) -> int:
    queue = []
    counter = 0
    for i in range(matrix_height):
        queue.append((i, 0))
    while queue:
        element = queue.pop(0)
        if element == (matrix_height - 1, matrix_width - 1) or element == (0, matrix_width - 1):
            counter += 1
        for neighbour in get_neighbours(element, matrix):
            queue.append(neighbour)
    return counter


def read_matrix_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extract W and H from the first line
        w, h = map(int, lines[0].split())

        # Extract the matrix from the remaining lines
        matrix = [list(line.strip()) for line in lines[1:]]

        return matrix, h, w
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def write_result_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


matrix = [['a', 'a', 'b'], ['a', 'a', 'a'], ['a', 'a', 'b']]
print(indiana_jones(matrix, 3, 3))
# matrix = [['a', 'a'], ['a', 'a'], ['a', 'a'], ['a', 'a']]
# print(indiana_jones(matrix, 2,2))
# input_file_path = 'ijones.in'
# output_file_path = 'ijones.out'
#
# matrix, matrix_height, matrix_width = read_matrix_from_file(input_file_path)
#
# result = indiana_jones(matrix, matrix_height, matrix_width)
# write_result_to_file(output_file_path, result)
