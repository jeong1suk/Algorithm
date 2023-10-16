def solution(brown, yellow):
    # 입력 : 갈색, 노란색의 갯수.
    size = brown + yellow
    # brown >= 8, yellow >= 1 이므로 x, y는 최소값이 3이다.
    
    for y in range(3, size):
        if size % y == 0: # 나누어 떨어질 때만
            x = size // y
            print(f"x={x}, y={y}")
            for yellow_block in range(y-2, 0, -2):
                if yellow // yellow_block < x-1 and yellow % yellow_block == 0:
                    print(f"원래노란색갯수: {yellow} / 감싸져있는 노란색: {yellow_block} = {yellow//yellow_block}")
                    return [x, y]
