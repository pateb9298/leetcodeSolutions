class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        array = []

        for i, value in enumerate(nums):
            complement = target - nums[i]
            if complement in seen:
                array.append(seen[complement])
                array.append(i)
                return array
            else:
                seen[value] = i

        return array
    
