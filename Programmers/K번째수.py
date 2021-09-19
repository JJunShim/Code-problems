def solution(array: list, commands: list) -> list:
    answer = [sorted(array[i-1:j])[k-1] for i, j, k in commands]
    return answer
