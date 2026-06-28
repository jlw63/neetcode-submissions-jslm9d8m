class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        #adjacency list
        hashmap = {}
        q = deque()
        visited = set()
        counter = 0
        hashmap[beginWord] = []
        for w in wordList:
            hashmap[w] = []
        word = wordList.copy()
        word.append(beginWord)
        size = len(word)
        
        for i in range(size):
            for j in range(i+1,size):
                count = 0
                for k in range(len(word[0])):
                    if word[i][k] != word[j][k]:
                        count += 1
                if count == 1:
                    hashmap[word[i]].append(word[j])
                    hashmap[word[j]].append(word[i])
        q.append(beginWord)
        visited.add(beginWord)
        if beginWord == endWord:
            return 1
        #bfs
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if node == endWord:
                    return counter +1
                for neighbours in hashmap[node]:
                    if neighbours not in visited:
                        visited.add(neighbours)
                        q.append(neighbours)
            counter += 1
        return 0
                        
                


        