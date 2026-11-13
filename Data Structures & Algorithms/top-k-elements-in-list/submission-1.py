class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iterdict = {}
        for i in nums:
            if i in iterdict:
                iterdict[i] += 1
            else:
                iterdict[i] = 0
        
        iterdict = dict(sorted(iterdict.items(), key=lambda items: items[1], reverse=True))
        return list(iterdict)[:k] 