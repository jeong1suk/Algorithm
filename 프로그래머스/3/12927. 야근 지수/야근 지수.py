def solution(n, works):
    answer = 0

    if sum(works) <= n: # 예외사항 처리
        return 0
    works.sort(reverse=True)
    while n > 0:
        max_val = works[0]
        
        # 최대값과 같은 수 찾기
        count = 0
        for w in works:
            if w == max_val:
                count += 1
            else:
                break
        # 다음 큰 값 계산
        next_val = works[count] if count < len(works) else 0
        
        diff = max_val - next_val
        need = diff * count
        
        if n >= need:
            # 한 번에 처리 가능
            for i in range(count):
                works[i] -= diff
            n -= need
        else:
            # 일부만 줄일 수 있음
            q, r = divmod(n, count)
            # print(f"q={q}, r={r}")
            for i in range(count):
                works[i] -= q
                if i < r:
                    works[i] -= 1
            n = 0
            
        works.sort(reverse=True)
    return sum(w ** 2 for w in works)