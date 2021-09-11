import heapq


def mixing(first, second):
    return first + second * 2


def solution(scoville: list, K: int):
    heap = []
    for n in scoville:
        heapq.heappush(heap, n)
    answer = 0
    a = heapq.heappop(heap)
    while a < K:
        try:
            mixed = mixing(a, heapq.heappop(heap))
        except:
            return -1
        else:
            a = heapq.heappushpop(heap, mixed)
        answer += 1
    return answer
