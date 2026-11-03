class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], speed[i]) for i in range(n)])

        times = [(target - cars[i][0]) / cars[i][1] for i in range(n)]

        fleet_count = 1
        running_max = times[n-1]
        for i in range(n-2, -1, -1):
            if times[i] > running_max:
                fleet_count += 1
                running_max = times[i]
        
        return fleet_count
