class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        Duplicate=False
        for i in range(len(nums)):
            if nums[i] in seen:
                Duplicate=True
            else:
                seen.add(nums[i])
        return(Duplicate)
