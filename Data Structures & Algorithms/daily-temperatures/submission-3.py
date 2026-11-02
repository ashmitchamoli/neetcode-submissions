class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        n = len(T)
        temps = {}
        result = [float('inf')] * n

        for i in range(n - 1, -1, -1):
            temps[T[i]] = i
            # print(i, T[i], temps)

            for temp in temps:
                if temp <= T[i]: continue
                if temps[temp] != 0:
                    result[i] = min(result[i], temps[temp] - i)
        
        return [0 if x == float('inf') else x for x in result]