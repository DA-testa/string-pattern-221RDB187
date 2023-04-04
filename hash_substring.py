def rabin_karp(pattern, text):
    P_len = len(pattern)
    P = hash(pattern)
    T_len = len(text)
    T = hash(text[:P_len])

    pos = []

    for _ in range(T_len - P_len + 1):
        if T == P:
            if text[_:_+P_len] == pattern:
                pos.append(_)
        if _ < T_len - P_len:
            T = hash(text[_+1:_+P_len+1])
    return pos
pattern = input()
pattern.strip()
text = input()
text.strip()

positions = rabin_karp(pattern, text)

print(*positions)
