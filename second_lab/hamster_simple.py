def max_hamsters(S, C, hamsters):
    hamsters.sort(key=lambda x: x[1])

    max_hamsters_count = 0
    total_food_needed = 0

    for i in range(C):
        daily_norm, greediness = hamsters[i]
        food_needed = daily_norm + greediness * i

        if total_food_needed + food_needed <= S:
            max_hamsters_count += 1
            total_food_needed += food_needed
        else:
            break

    return max_hamsters_count


S1 = 7
C1 = 3
hamsters1 = [[1, 2], [2, 2], [3, 1]]
print(max_hamsters(S1, C1, hamsters1))

S2 = 19
C2 = 4
hamsters2 = [[5, 0], [2, 2], [1, 4], [5, 1]]
print(max_hamsters(S2, C2, hamsters2))

S3 = 2
C3 = 2
hamsters3 = [[1, 50000], [1, 60000]]
print(max_hamsters(S3, C3, hamsters3))

print(max_hamsters(109, 4, [[107, 1], [1,0], [1000, 0]]))
print(max_hamsters(12, 3, [[1, 2], [1,0], [2, 3]]))