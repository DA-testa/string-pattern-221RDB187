#221RDB187
def read_input():
    inp = input().rstrip()

    if "F" in inp:
        with open('./tests/06', 'r') as fails:
            pattern = fails.readline().rstrip()
            text = fails.readline().rstrip()
        return (pattern.rstrip(), text.rstrip())
    elif "I" in inp:
        pattern = fails.readline().rstrip()
        text = fails.readline().rstrip()
    else:
        print("Input error")
    return(pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    P_len = len(pattern)
    T_len = len(text)

    if T_len < P_len:
        return []
    

    pos = []
    P = 0
    T = 0
    c = 256
    p = 13
    h = 1

    for i in range(P_len - 1):
        h = (h * c) % p
    

    for i in range(P_len):
        P = (c * P + ord(pattern[i])) % p
        T = (c * T + ord(text[i])) % p
        
    for i in range(T_len - P_len + 1):
        if T == P and pattern == text[i:i + P_len] :
                pos.append(i)
        if i < T_len - P_len:
            T = (c * (T - ord(text[i]) * h) + ord(text[i + P_len])) % p
            T = (T + p) % p

    return pos

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
