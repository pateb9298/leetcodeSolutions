class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        result = [1]*len(nums)

        first = 1
        for i in range(1, len(nums)):
            prefix[i] = first * nums[i-1]
            first = prefix[i]

        last = 1
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = last * nums[i+1]
            last = suffix[i]
        
        for i in range(len(result)):
            result[i] = prefix[i] * suffix[i]

        return result