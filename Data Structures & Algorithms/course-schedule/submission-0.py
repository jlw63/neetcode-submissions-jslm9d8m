class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap_pre = {}
        hashmap_count = {}
        taken = 0
        hashmap_count = {i:0 for i in range(numCourses)}       
        for p in prerequisites:
            if p[1] not in hashmap_pre:
                hashmap_pre[p[1]] = []
            hashmap_pre[p[1]].append(p[0])
            hashmap_count[p[0]] += 1
        q = deque()
        for c in hashmap_count:
            if hashmap_count[c] == 0:
                q.append(c)
        while q:
            taken+= 1
            course = q.popleft()
            for next_course in hashmap_pre.get(course, []):
                hashmap_count[next_course] -= 1

                if hashmap_count[next_course] == 0:
                    q.append(next_course)
        if taken == numCourses:
            return True
        return False