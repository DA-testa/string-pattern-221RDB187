# python3
# 221RDB187
def read_input():
    inp = input()
    if "F" in inp:
        with open(str("./tests/06"), mode="r") as fails:
            pattern = fails.readline()
            text = fails.readline()
        return (pattern.rstrip(), text.rstrip())
    elif "I" in inp:
        return (input().rstrip(), input().rstrip())
    else:
        print("Input error")

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    P_len = len(pattern)
    P = hash(pattern)
    T_len = len(text)
    T = hash(text[:P_len])
    pos = []

    for i in range(T_len - P_len + 1):
        if T == P:
            if text[i:i+P_len] == pattern:
                pos.append(i)
        if i < T_len - P_len:
            T = hash(text[i+1:i+P_len+1])
    
    return pos

pattern = input()
text = input()


if __name__ == '__main__':
    print_occurrences(get_occurrences(pattern, text))
