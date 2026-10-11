class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for s in strs:
            k = tuple(sorted(s))
            if k not in groupings:
                groupings[k] = []
            
            groupings[k].append(s)
        
        return list(groupings.values())