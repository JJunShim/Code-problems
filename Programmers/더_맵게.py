import heapq


def solution(scoville: list, K: int) -> int:
    heapq.heapify(scoville)
    mixed = heapq.heappop(scoville)
    answer = 0
    while mixed < K:
        try:
            mixed += heapq.heappop(scoville) * 2
        except:
            return -1
        mixed = heapq.heappushpop(scoville, mixed)
        answer += 1
    return answer
