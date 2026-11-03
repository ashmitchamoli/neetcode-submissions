class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        n = len(T)
        result = [0] * n
        st = []

        for i in range(n):
            while len(st) > 0 and T[st[-1]] < T[i]:
                l = st.pop()
                result[l] = i - l
            
            st.append(i)
        
        return result