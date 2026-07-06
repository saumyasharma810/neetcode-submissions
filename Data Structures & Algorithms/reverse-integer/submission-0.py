class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        t = 0
        x = abs(x)
        # length = 0
        while x:
            if t > 0 and math.log2(t) + math.log2(10) > 31:
                return 0
            if t > 0 and not neg and math.log2(t) + math.log2(10) == 31:
                return 0
            t = t*10 + x%10
            x//=10
        print(t)
        return -1*t if neg else t

        