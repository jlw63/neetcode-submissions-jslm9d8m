class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        h = []
        d = deque()
        for i in tasks:
            counts[i] = counts.get(i, 0) + 1
        counts = [-c for c in counts.values()]
        heapq.heapify(counts)
        h = counts
        time = 0
        q = deque() #pairs of [-c, idletime]

        while h or q:
            time += 1
            if h:
                c = 1 + heapq.heappop(h)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] <= time:
                heapq.heappush(h, q.popleft()[0])
        return time
            


        