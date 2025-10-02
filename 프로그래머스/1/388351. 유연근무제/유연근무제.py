def time_to_minute(time):
    hour = time // 100
    minute = time % 100
    return hour * 60 + minute
def solution(schedules, timelogs, startday):
    n = len(schedules)
    
    for i in range(n):
        hope = time_to_minute(schedules[i])
        # 실제통근시간은 timelogs
        for j in range(len(timelogs[i])):
            idx = (j + startday) % 7            
            if idx == 0 or idx == 6:
                continue
            real = time_to_minute(timelogs[i][j])
            if real > hope + 10:
                n -= 1
                break
    return n