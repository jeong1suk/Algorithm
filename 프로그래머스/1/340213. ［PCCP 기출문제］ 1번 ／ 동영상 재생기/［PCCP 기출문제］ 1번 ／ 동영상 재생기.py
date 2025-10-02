def solution(video_len, pos, op_start, op_end, commands):
    def time_split(time):
        time_split = time.split(":")
        return int(time_split[0]) * 60 + int(time_split[1])

    _video_len = time_split(video_len) # 전체 길이
    _pos = time_split(pos) # 현재 위치
    _op_start, _op_end = time_split(op_start), time_split(op_end)
    
    for com in commands:
        if _op_start <= _pos and _pos < _op_end:
            _pos = _op_end
        
        if com in ('next', 'prev'):
            _pos += 10 if com == 'next' else -10
            _pos = max(0, min(_pos, _video_len))
    if _op_start <= _pos and _pos < _op_end:
            _pos = _op_end
        
    return f"{_pos // 60:02}:{_pos % 60:02}"