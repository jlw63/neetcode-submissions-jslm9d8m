class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        queue = deque()
        for i in range(len(tasks)):
            hashmap[tasks[i]] = hashmap.setdefault(tasks[i],0) +1
        freq = list(hashmap.values())
        freq = [-f for f in freq]
        heapq.heapify(freq)
        timer = 0
        while freq or queue:
            timer += 1
            if freq:

                temp = heapq.heappop(freq)
                rem = temp + 1
                if rem < 0:
                    queue.append((rem, timer + n ))

            if queue:
                if queue[0][1] == timer:
                    temp = queue.popleft()
                    heapq.heappush(freq,temp[0])

        return timer


        