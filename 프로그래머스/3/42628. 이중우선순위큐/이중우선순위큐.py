def solution(operations):
    heap = list()
    for command in operations:
        op, num = command.split()
        num = int(num)
        if op == 'I':
            heap.append(num)
            heap.sort()
        elif op == 'D' and heap:
            if num == -1:
                heap.pop(0)
            else:
                heap.pop()

    return [heap[-1], heap[0]] if heap else [0,0]