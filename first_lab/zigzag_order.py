def zigzag_order(array: list[list[int]]) -> list:
    i, j = 0, 0
    m, n = len(array), len(array[0])
    order_list = [array[i][j]]
    if n == 1:
        for i in range(1, m):
            order_list.append(array[i][0])
        return order_list

    if m == 1:
        for j in range(1, n):
            order_list.append(array[0][j])
        return order_list

    if m == 2 and n % 2 != 0:
        while j + 2 < n:
            j += 1
            order_list.append(array[i][j])
            while i != 1:
                j -= 1
                i += 1
                order_list.append(array[i][j])
            j += 1
            order_list.append(array[i][j])
            while i != 0:
                j += 1
                i -= 1
                order_list.append(array[i][j])
        i += 1
        order_list.append(array[i][j])
        return order_list

    if m == 2 and n % 2 == 0:
        while j + 1 < n:
            j += 1
            order_list.append(array[i][j])
            while i != 1:
                j -= 1
                i += 1
                order_list.append(array[i][j])
            j += 1
            order_list.append(array[i][j])
            if j + 1 != n:
                while i != 0:
                    j += 1
                    i -= 1
                    order_list.append(array[i][j])
            else:
                return order_list

    if m == 3 and n % 2 != 0:
        j += 1
        order_list.append(array[i][j])
        j -= 1
        i += 1
        order_list.append(array[i][j])
        i += 1
        order_list.append(array[i][j])
        while j + 2 != n - 1:
            while i != 0:
                j += 1
                i -= 1
                order_list.append(array[i][j])
            j += 1
            order_list.append(array[i][j])
            while i != 2:
                j -= 1
                i += 1
                order_list.append(array[i][j])
            j += 1
            order_list.append(array[i][j])
        while i != 0:
            j += 1
            i -= 1
            order_list.append(array[i][j])
        i += 1
        order_list.append(array[i][j])
        j -= 1
        i += 1
        order_list.append(array[i][j])
        j += 1
        order_list.append(array[i][j])
        return order_list

    '''case 3+'''
    while j + 2 < n:
        j += 1
        order_list.append(array[i][j])
        while j != 0:
            j -= 1
            i += 1
            order_list.append(array[i][j])
        i += 1
        order_list.append(array[i][j])
        while i != 0:
            i -= 1
            j += 1
            order_list.append(array[i][j])
    j += 1
    order_list.append(array[i][j])
    j -= 1
    while i + 2 < m:
        i += 1
        order_list.append(array[i][j])
        while i != m - 1:
            j -= 1
            i += 1
            order_list.append(array[i][j])
        j += 1
        order_list.append(array[i][j])
        while j != n - 1:
            i -= 1
            j += 1
            order_list.append(array[i][j])


    return order_list


"""print(zigzag_order([[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30],
                    [31, 32, 33, 34, 35, 36]]))"""
print(zigzag_order([[1,2,3],
                    [4,5,6],
                    [7,8,9]]))
