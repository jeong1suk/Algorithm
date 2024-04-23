def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b / gcd(a,b)
def solution(arr):
    answer = 1
    for num in arr:
        answer = lcm(answer, num)

    return answer