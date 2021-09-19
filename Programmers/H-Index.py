def solution(citations: list) -> int:
    citations.sort()
    answer = len(citations)
    while sum(_ >= answer for _ in citations) < answer:
        answer -= 1
    return answer
