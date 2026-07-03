class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Saved_value={}
        for i in range (len(nums)):
            if nums[i] in Saved_value:
                return [Saved_value[nums[i]], i]
            else:
                Saved_value[target - nums[i]] = i 
       
        
               
                