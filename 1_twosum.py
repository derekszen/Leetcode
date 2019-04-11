class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # returns a list with two indices corresponding to original nums list. adds up to Target
        # assume exactly one solution
        # O(n) solution
        diffmap = {}
        for (index, num) in enumerate(nums):
            complement = target - num
            if complement in diffmap:
                return [diffmap[complement], index]
            diffmap[num] = index
