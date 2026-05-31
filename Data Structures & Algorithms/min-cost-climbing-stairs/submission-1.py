class Solution:
    def minCostClimbingStairs(self, cost: List[int],i = 0, notepad = None) -> int:
        if notepad is None:
            notepad = {}
        #base case
        if i >= len(cost):
            return 0
        #notepadcheck
        if i in notepad:
            return notepad[i]

        future1 = self.minCostClimbingStairs(cost, i+ 1, notepad)
        future2 = self.minCostClimbingStairs(cost, i+ 2, notepad)
        total_cost = cost[i] +min(future1, future2)
        notepad[i] = total_cost

        if i == 0:
            cost_from1 =self.minCostClimbingStairs(cost, 1, notepad)
            if total_cost < cost_from1:
                return total_cost
            else:
                return cost_from1
        return total_cost
        