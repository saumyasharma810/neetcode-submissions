class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = []
        for i in range(len(position)):
            cars.append((position[i],(target-position[i])/speed[i]))
        cars.sort(reverse = True)
        prev = float("-inf")
        for i in range(len(cars)):
            if cars[i][1] > prev:
                fleets+=1
            prev = max(cars[i][1],prev)
        return fleets
            

        