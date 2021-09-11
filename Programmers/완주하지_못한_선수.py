def solution(participant, completion):
    d = {hash(_): _ for _ in participant}
    def f(x): return sum(map(hash, x))
    return d[f(participant) - f(completion)]


def solution(participant: list, completion: list):
    answer = ''
    part, comp = map(sorted, (participant, completion))
    for p, c in zip(part, comp):
        if p != c:
            answer = p
            break
    else:
        answer = part[-1]
    return answer
