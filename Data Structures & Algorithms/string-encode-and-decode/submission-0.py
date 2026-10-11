class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = suffix = ""
        
        for s in strs:
            prefix += str(len(s)) + ","
            suffix += s
        
        final = prefix + '*' + suffix

        return final

    def decode(self, s: str) -> List[str]:
        prefix, suffix = s.split("*", 1)
        lens = prefix.split(",")

        final = []
        total = 0
        for l in lens[:-1]:
            final.append(suffix[total:total+int(l)])
            total+=int(l)
        
        return final
