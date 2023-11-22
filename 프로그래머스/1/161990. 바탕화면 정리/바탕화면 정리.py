def solution(wallpaper):
    # answer = [100,100, 0, 0]
    lux, luy, rdx, rdy = 100, 100, 0, 0
    # print(wallpaper)
    for idx, point in enumerate(wallpaper):
        for i in range(0, len(point)): # 왼쪽 좌표 설정하기
            if point[i] == '#': # 파일이 존재
                if lux == 100:
                    lux = idx
                if luy > i:
                    luy = i
                break
        for i in range(len(point)-1, -1, -1): # 오른쪽 좌표 설정하기
            if point[i] == "#":
                rdx = idx + 1
                if rdy <= i:
                    rdx, rdy = idx+1, i+1
    return [lux, luy, rdx, rdy]