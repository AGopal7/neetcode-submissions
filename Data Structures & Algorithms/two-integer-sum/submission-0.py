class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Save_value = {}
        for i in range (len(nums)):
            if nums[i] in Save_value:
                return [ Save_value[nums[i]], i]
            else:
                Save_value[target - nums[i]]= i 
                