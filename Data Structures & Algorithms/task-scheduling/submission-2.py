class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = [-c for c in count.values()]
        heapq.heapify(count)
        d = deque()
        time = 0
        while count or d:
            time += 1
            if count:
                c = 1 + heapq.heappop(count)
                if c:
                    d.append([c, time + n])
            if d and d[0][1] == time:
                heapq.heappush(count, d.popleft()[0])
        return time





        