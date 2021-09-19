def hash_sum(x: list) -> int:
    return sum(map(hash, x))


def solution(participant: list, completion: list) -> str:
    dic = {hash(_): _ for _ in participant}
    key = hash_sum(participant) - hash_sum(completion)
    return dic.get(key)


def solution(participant: list, completion: list) -> str:
    part, comp = map(sorted, (participant, completion))
    answer = part[-1]
    for p, c in zip(part, comp):
        if p != c:
            answer = p
            break
    return answer
