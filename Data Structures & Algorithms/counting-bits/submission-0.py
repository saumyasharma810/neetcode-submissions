class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1)
        nearest_power = 0
        next_power = 1
        for i in range(1, n+1):
            if i == next_power:
                bits[i] = 1
                nearest_power = next_power
                next_power *= 2
                continue
            bits[i] = 1 + bits[i-nearest_power]
        return bits
            

            


        