class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        iterdict = {}
        for i in range(len(nums)):
            if nums[i] in iterdict:
                iterdict[nums[i]] += 1
            else:
                iterdict[nums[i]] = 1
        finaldict = {k:v for v,k in iterdict.items()}
        return finaldict[max(finaldict.keys())]