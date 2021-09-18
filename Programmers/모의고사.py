from math import ceil


def solution(answers: list):
    students = (1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4,
                                 2, 5), (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    answer = []
    n = 0
    for k, v in enumerate(students, 1):
        m = sum(a == b for a, b in zip(
            answers, v * ceil(len(answers) / len(v))))
        if n <= m:
            if n < m:
                answer = []
                n = m
            answer.append(k)

    return answer
