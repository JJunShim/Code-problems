def solution(priorities: list, location: int) -> int:
    answer = 1
    while priorities:
        maxvalue = max(priorities)
        if not location:
            if priorities[location] == maxvalue:
                break
            location += len(priorities)
        temp = priorities.pop(0)
        if temp != maxvalue:
            priorities.append(temp)
        else:
            answer += 1
        location -= 1
    return answer
