class Solution:
    def isHappy(self, n: int) -> bool:
        seen_num = set()
        seen_num.add(n)
        x = n
        while True:
            summation = 0
            while x:
                summation += ((x%10) ** 2)
                x//=10
            print(summation)
            if summation == 1:
                return True
            if summation in seen_num:
                return False
            seen_num.add(summation)
            x = summation
        