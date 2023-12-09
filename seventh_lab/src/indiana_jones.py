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
    return neigh_list


def indiana_jones(matrix: list[list[str]]) -> int:
    matrix_height, matrix_width = len(matrix), len(matrix[0])
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


matrix = [["a", 'b', 'a'],
          ['a', 'c', 'b'],
          ['a', 'f', 'e'],
          ['a', 'g', 'a']]

print(get_neighbours((1, 0), matrix))
print(indiana_jones(matrix))
