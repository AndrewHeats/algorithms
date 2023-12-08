def next_state(pattern: str, length: int, state: int, x: str):
    if state < length and ord(pattern[state]) == x:
        return state + 1
    idx = 0
    for nxt_state in range(state, 0, -1):
        if ord(pattern[nxt_state - 1]) == x:
            while idx < nxt_state - 1:
                if pattern[idx] != pattern[state - nxt_state + 1 + idx]:
                    break
                idx += 1
            if idx == nxt_state - 1:
                return nxt_state
    return 0


def create_t_f(pattern, length):
    TF = [[0 for i in range(256)] for _ in range(length + 1)]
    for state in range(length + 1):
        for x in range(256):
            state_number = next_state(pattern, length, state, x)
            TF[state][x] = state_number

    return TF


def finite_automata_search(needle, haystack):
    ocurrence_list = []
    pattern_length = len(needle)
    text_length = len(haystack)
    TF = create_t_f(needle, pattern_length)
    state = 0
    for i in range(text_length):
        state = TF[state][ord(haystack[i])]
        if state == pattern_length:
            ocurrence_list.append(i - pattern_length + 1)
    return ocurrence_list
