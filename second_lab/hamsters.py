def greedy_sort(h_list):
    n = len(h_list)
    for i in range(1, n):
        key = h_list[i]
        j = i - 1
        while j >= 0 and h_list[j][1] > key[1]:
            h_list[j + 1] = h_list[j]
            j -= 1
        h_list[j + 1] = key
    return h_list


def hunger_sort(h_list):
    n = len(h_list)
    for i in range(1, n):
        key = h_list[i]
        j = i - 1
        while j >= 0 and h_list[j][0] > key[0]:
            h_list[j + 1] = h_list[j]
            j -= 1
        h_list[j + 1] = key
    return h_list


def hamsters(S: int, C: int, hamster_list: list[list[int]]) -> int:
    hungry_list = hunger_sort(hamster_list)
    max_hungry_idx = 0
    hungry_corm = 0
    while S >= hungry_corm and max_hungry_idx <= C:
        hungry_corm = 0
        max_hungry_idx += 1
        for i in range(max_hungry_idx):
            hungry_corm += hungry_list[i][0]
            hungry_corm += hungry_list[i][1] * (max_hungry_idx - 1)

    greedy_list = greedy_sort(hamster_list)
    max_greedy_idx = 0
    greedy_corm = 0
    while S >= greedy_corm and max_hungry_idx <= C:
        greedy_corm = 0
        max_greedy_idx += 1
        for i in range(max_greedy_idx):
            greedy_corm += greedy_list[i][0]
            greedy_corm += greedy_list[i][1] * (max_greedy_idx - 1)

    if max_greedy_idx > max_hungry_idx:
        return max_greedy_idx - 1
    return max_hungry_idx - 1

print(hamsters(109, 1, [[1000, 1000]]))
