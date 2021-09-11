def solution(citations: list):
    citations.sort()
    answer = len(citations)
    while len([_ for _ in citations if _ >= answer]) < answer:
        answer -= 1
    return answer
