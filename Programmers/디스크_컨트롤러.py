import heapq


def solution(jobs: list) -> int:
    answer, now, i = (0, ) * 3
    start = -1
    heap = []
    while i < len(jobs):
        for request, need in jobs:
            if start < request <= now:
                heapq.heappush(heap, (need, request))
        if heap:
            need, request = heapq.heappop(heap)
            start = now
            now += need
            answer += now - request
            i += 1
        else:
            now += 1
    answer //= len(jobs)
    return answer
