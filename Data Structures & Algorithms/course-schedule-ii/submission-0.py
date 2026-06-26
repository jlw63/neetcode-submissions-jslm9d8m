class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        indeg = {}
        q = deque()
        result = []
        indeg = {i:0 for i in range(numCourses)}
        for p in prerequisites:
            if p[1] not in prereq:
                prereq[p[1]] = []
            prereq[p[1]].append(p[0])
            indeg[p[0]] += 1

        for i in indeg:
            if indeg[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            result.append(course)
            for next_course in prereq.get(course,[]):
                indeg[next_course] -= 1

                if indeg[next_course] == 0:
                    q.append(next_course)
        if len(result) != numCourses:
            return []
        return result


        