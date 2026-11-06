class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        iterdict = {}
        iterlist = []
        for i in strs:
            keyd = ''.join(sorted(i))
            if keyd not in iterdict:
                iterdict[keyd] = [i]
            else:
                iterdict[keyd].append(i)
        return list(iterdict.values())
                