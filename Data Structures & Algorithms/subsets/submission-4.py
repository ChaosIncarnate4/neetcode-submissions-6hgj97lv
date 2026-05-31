class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def helper(currList, nums):
            if not nums:
                ans.add(tuple(sorted(currList)))
                return
            helper(currList, nums[1:])
            helper(currList + [nums[0]], nums[1:])
            
        helper([], nums)
        return [list(i) for i in ans]