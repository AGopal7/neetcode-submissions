class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Saved_value = {}
        for i in range (len(nums)):

            if nums[i] in Saved_value :

                #print(f" the number {nums[i]} already exists in the list at position{i}"  )
                return True
                
            else:
                Saved_value[nums[i]] = True
        return False