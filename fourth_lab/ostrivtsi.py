def get_neighbours(matrix: list[list[int]], current_vertex: list[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    height, width = tuple(current_vertex)
    size = len(matrix)
    if matrix[height][width] != 0:
        if height != size - 1:
            if matrix[height + 1][width] == 1:
                neighbours.append([height + 1, width])

        if width != size - 1:
            if matrix[height][width + 1] == 1:
                neighbours.append([height, width + 1])

        if width != 0:
            if matrix[height][width - 1] == 1:
                neighbours.append([height, width - 1])

        if height != 0:
            if matrix[height - 1][width] == 1:
                neighbours.append([height - 1, width])
        # diagonal neighbours
        if height != size - 1 and width != size - 1:
            if matrix[height + 1][width + 1] == 1:
                neighbours.append([height + 1, width + 1])

        if width != size - 1 and height != 0:
            if matrix[height - 1][width + 1] == 1:
                neighbours.append([height - 1, width + 1])

        if width != 0 and height != size - 1:
            if matrix[height + 1][width - 1] == 1:
                neighbours.append([height + 1, width - 1])

        if height != 0 and width != 0:
            if matrix[height - 1][width - 1] == 1:
                neighbours.append([height - 1, width - 1])
        return neighbours
    return []


def get_all_neighbours(matrix: list[list[int]], current_vertex: list[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    queue = [current_vertex]
    while queue:
        current_element = queue.pop(0)
        for neighbour in get_neighbours(matrix, current_element):
            if neighbour not in neighbours:
                queue.append(neighbour)
        if current_element not in neighbours:
            neighbours.append(current_element)
    return neighbours


def get_count_of_islands(matrix: list[list[int]]) -> int:
    current_element = [0, 0]
    count = 1
    while current_element != [len(matrix) - 1, len(matrix) - 1]:
        if len(get_neighbours(matrix, current_element)) >= 2 and matrix[current_element[0]][current_element[1]] == 1:
            for neighbour in get_all_neighbours(matrix, current_element):
                height, width = neighbour
                count += 1
                matrix[height][width] = count
        current_element[1] += 1
        if current_element[1] >= len(matrix):
            current_element[0] += 1
            current_element[1] = 0
    return count - 1


matrix = []
print(get_neighbours(matrix, [3, 1]))
print(get_all_neighbours(matrix, [3, 1]))
print(get_count_of_islands(matrix))
