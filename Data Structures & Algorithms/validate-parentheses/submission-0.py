class Solution:
    def isValid(self, s: str) -> bool:
        closer = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        st = []

        for c in s:
            top = st[-1] if st else ""

            if top in closer and closer[top] == c:
                st.pop()
            else:
                st.append(c)
        
        return st == []