class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        l = 0
        total = 0
        for i in range(32):
            a_bit = a >> i & 1
            b_bit = b >> i & 1
            sum_bit = a_bit ^ b_bit ^ c
            c = a_bit&b_bit | a_bit&c | b_bit&c
            if sum_bit:
                sum_bit = sum_bit << l
                total = total | sum_bit
            l+=1
            # print(a,b,c)
        if total > 0x7FFFFFFF:
            total = ~(total^0xFFFFFFFF)
        return total





        
        