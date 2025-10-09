import math

def solution(progresses, speeds):
    answer = []
    # print("먼저 배포되어야 하는 순서:", progresses)
    # print("각 작업의 개발 속도:", speeds)

    i = 0
    n = len(progresses)

    while i < n:
        # i번째 작업이 완료되는데 걸리는 일수
        day = math.ceil((100 - progresses[i]) / speeds[i])
        # print(f"\n현재 인덱스 {i}, 기준 작업 완료 예상일: {day}일")

        count = 1  # 첫 번째 작업은 반드시 포함됨

        # 다음 작업들이 같은 날 또는 이전에 끝나는지 확인
        for j in range(i + 1, n):
            day2 = math.ceil((100 - progresses[j]) / speeds[j])
            # print(f"  작업 {j} 완료 예상일: {day2}일")
            if day2 <= day:
                count += 1
                # print(f"  함께 배포 가능 (누적 {count}개)")
            else:
                # print(f"  이후 작업은 다음 배포로 넘어감")
                break

        answer.append(count)
        i += count  # 다음 배포 그룹으로 이동

    # print("\n최종 배포 묶음:", answer)
    return answer