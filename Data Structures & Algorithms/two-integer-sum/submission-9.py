class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iterdict={}
        for index, need in enumerate(nums):
            if target-need in iterdict:
                return [iterdict[target-need], index]
            iterdict[need]=index