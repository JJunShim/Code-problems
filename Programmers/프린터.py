def solution(priorities: list, location: int) -> int:
    answer = 1
    while priorities:
        maxvalue = max(priorities)
        if not location:
            if priorities[location] == maxvalue:
                break
            location += len(priorities)
        temp = priorities.pop(0)
        if temp == maxvalue:
            answer += 1
        else:
            priorities.append(temp)
        location -= 1
    return answer
