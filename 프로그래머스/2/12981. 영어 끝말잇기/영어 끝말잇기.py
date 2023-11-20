def solution(n, words):
    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

# 나머지가 걸린 사람, 차례 -> 몫 올림
# idx=8, idx%n + 1 = 3, idx/n 올림하기
    for idx, word in enumerate(words):
        if idx == 0:
            continue
            
        if word[0] != words[idx-1][-1] or word in words[:idx]:
            # print(word[0], words[idx-1][-1])
            # print(f"idx={idx}, word={word}")
            return [idx%n+1, idx//n+1]
        

    return [0,0]