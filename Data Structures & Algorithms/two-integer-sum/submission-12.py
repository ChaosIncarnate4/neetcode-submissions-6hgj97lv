class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i in range(len(nums)):
            counter = target - nums[i]
            if counter in numDict:
                return [numDict[counter], i]
            else:
                numDict[nums[i]] = i
        
        return [-1, -1]