class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = nums[0]
        localMin = nums[0]
        globalMax = nums[0]

        for i in range(1,len(nums)):
            localMax = nums[0]
        localMin = nums[0]
        globalMax= nums[0]

        for i in range(1, len(nums)):
            if nums[i]<0:
                localMax, localMin = localMin, localMax
            localMax = max(nums[i], localMax*nums[i])
            localMin = min(nums[i], localMin *nums[i])
            globalMax = max(globalMax, localMax)
        return globalMax