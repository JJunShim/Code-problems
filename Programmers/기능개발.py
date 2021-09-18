def distribute(progress: int, speed: int):
    try:
        quotient, remainder = divmod(100 - progress, speed)
    except:
        return 0
    return quotient + bool(remainder)


def solution(progresses: list, speeds: list):
    days = [distribute(*n) for n in zip(progresses, speeds)]
    answer = []
    i = 0
    for j, day in enumerate(days):
        if day > days[i]:
            answer.append(j - i)
            i = j
    answer.append(len(days) - i)
    return answer
