def solution(numbers: list, target: int) -> int:
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    answer = leaves.count(target)
    return answer
