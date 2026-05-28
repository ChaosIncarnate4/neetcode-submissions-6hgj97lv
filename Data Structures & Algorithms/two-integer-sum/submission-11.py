class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            counter = target - nums[i]
            if counter in dict:
                return [dict[counter], i]
            dict[nums[i]] = i
        
        return []