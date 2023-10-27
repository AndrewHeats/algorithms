def get_neighbours(matrix: list[list[int]], current_vertex: list[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    height, width = tuple(current_vertex)
    size = len(matrix)
    if matrix[height][width] == 1:
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
    return None

def broad_first_search(matrix, current_vertex, visited):
    queue = [current_vertex]
    visited.add(current_vertex)

    while queue:
        current_vertex = queue.pop(0)
        for neighbour in get_neighbours(matrix, current_vertex):
            if tuple(neighbour) not in visited:
                queue.append(neighbour)
                visited.add(tuple(neighbour))

def get_count_of_islands(matrix):
    if not matrix:
        return 0
    size = len(matrix)
    visited = set()
    count = 0

    for height in range(size):
        for width in range(size):
            if matrix[height][width] == 1 and (height, width) not in visited:
                broad_first_search(matrix, (height, width), visited)
                count += 1

    return count


matrix = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
          [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
          [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
          [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]

print(get_count_of_islands(matrix))