# python3
# 221RDB187
def read_input():
    inp = input()
    if "F" in inp:
        with open(str("./tests/06"), mode="r") as fails:
            pattern = fails.readline()
            text = fails.readline()
        return (pattern.rstrip().lower(), text.rstrip().lower())
    elif "I" in inp:
        return (input().rstrip(), input().rstrip())
    else:
        print("Input error")

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    P_len = len(pattern)
    c = 256
    T_len = len(text)
    p = 101
    h = pow(c, P_len - 1) % p
    pos = []
    P = 0
    T = 0

    for i in range(P_len):
        P = (c * P + ord(pattern[i])) % p
        T = (c * T + ord(text[i])) % p
        
    for i in range(T_len - P_len + 1):
        if T == P:
            if text[i:i + P_len] == pattern:
                pos.append(i)
        if i < T_len - P_len:
            T = (c * (T - ord(text[i]) * h) + ord(text[i + P_len]))% p
            if T < 0:
                T += p


    return pos

pattern = input()
text = input()


if __name__ == '__main__':
    print_occurrences(get_occurrences(pattern, text))
