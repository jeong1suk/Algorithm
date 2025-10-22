def make_full_tree(n: int) -> str:
    b = bin(n)[2:]
    h = 1
    while (1 << h) - 1 < len(b):
        h += 1
    full_len = (1 << h) - 1
    print(full_len)
    return b.rjust(full_len, "0")

def check(s: str) -> bool:
    if not s:
        return True
    if '1' not in s:
        return True
    mid = len(s) // 2
    if s[mid] == '0':
        return False
    return check(s[:mid]) and check(s[mid+1:])

def solution(numbers):
    answer = []
    # s = "110000010000000"
    # print(check(s))
    for n in numbers:
        b = make_full_tree(n)
        answer.append(1 if check(b) else 0)
    return answer