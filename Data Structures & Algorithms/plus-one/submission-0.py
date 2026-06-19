class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        new_list = []
        for i in range(len(digits)-1, -1, -1):
            new_list.append((digits[i]+carry)%10)
            carry = (digits[i]+carry)//10
            
        
        if carry == 1:
            new_list.append(1)
        
        new_list.reverse()
        return new_list



        