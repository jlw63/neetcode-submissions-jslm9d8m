class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []        # This will hold all of our final subsets
        current = []    # This tracks the subset we are building right now
        
        def backtrack(i):
            # 1. BASE CASE
            # If i has reached the end of nums, we are done with this path!
            if i == len(nums):
                res.append(current.copy()) # We take a snapshot of current
                return
            
            # 2. THE "INCLUDE" CHOICE
            # What do you need to add to 'current' before moving to the next index?

            current.append(nums[i])
            
            backtrack(i + 1) # Recurse to the next number
            
            # 3. THE BACKTRACK (UNDO)
            # You finished exploring the "Include" path. 
            # Now pop that number back out of 'current' so it's clean!
            # (Fill this in)
            current.pop()

            
            # 4. THE "SKIP" CHOICE
            # Now explore what happens if that number was never there.
            backtrack(i + 1) # Recurse to the next number without adding anything
            
        # Start the backtracking at index 0
        backtrack(0)
        return res