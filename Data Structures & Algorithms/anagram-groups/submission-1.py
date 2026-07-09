class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sort = "".join(sorted(i))
            hashmap[sort].append(i)
        return list(hashmap.values())
        