from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    # print(records[0].split(" "))
    park_time = defaultdict(int) # 주차 시간 관리
    out_records = defaultdict(bool) # 입출차 관리
    # parking_records[5961] = 100
    # out_records[5961] = False
    # print(parking_records, out_records)
    # t = records[0].split(" ")[0].split(":")
    # print(t, int(t[0]) * 60 + int(t[1]))
    
    for record in records:
        time, cnum, inout = record.split(" ")
        h = int(time.split(":")[0])
        m = int(time.split(":")[1])
        pt = h * 60 + m # 입출차 시각
        # print(f"time={time}, {h*60+m}, 자동차 번호={cnum}, 입출차={inout}")
        if inout == "IN":
            park_time[cnum] -= pt
            out_records[cnum] = False
        else:
            park_time[cnum] += pt
            out_records[cnum] = True # 출차하면 True
        # print(park_time, out_records)
    for n in out_records:
        if not out_records[n]:
            # print(f"{n} 출차 안 함")
            park_time[n] += (23*60 + 59) # 출차 안한 차량 23:59분에 나가게
    ttime, pprice, mminute, ffee = fees
    # print(park_time)
    # print(ttime, pprice, mminute, ffee)
    # print(154/10, int(154/10))
    new_park_time = sorted(park_time.items())
    for cn, pt in new_park_time:
        # print(cn, pt)
        # cn은 차량번호, sort하기
        # pt는 주차된 시간
        money = pprice + math.ceil(max(pt - ttime, 0)/mminute) * ffee
        # print(f"{cn}의 요금={money}")
        answer.append(money)
        
    return answer
'''
시간은 초로 변환해서 계산, defaultdict로 하면 편한가
IN, OUT이 바로바로 들어오는게 아님, 2번 이상 가능
records의 원소들은 시각을 기준으로 오름차순 정렬
IN이면 -, OUT이면 +
ex 300 IN = -300 / 360 OUT -300 + 360 = 60 60분동안 주차된건 맞음
여기서 480 IN 600 OUT이면 60 - 480 + 600 = -420 + 600 = 180
OUT 됐는지 확인해야함
'''