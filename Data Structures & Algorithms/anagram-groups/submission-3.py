class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for s in strs:
            k = str(sorted(s))
            if k not in groupings:
                groupings[k] = []
            
            groupings[k].append(s)
        
        return list(groupings.values())