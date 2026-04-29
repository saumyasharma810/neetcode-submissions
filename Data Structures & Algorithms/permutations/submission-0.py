class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        for i in range(1,len(nums)):
            res_copy = []
            for perm in res:
                print(perm,"perm")
                perm_copy = [perm.copy()]
                perm_copy *= (i+1)
                k = 0
                print(perm_copy,"perm_copy")
                for p in perm_copy:
                    print(p,"p")
                    p_copy = p.copy()
                    p_copy.insert(k,nums[i])
                    k+=1
                    res_copy.append(p_copy)
            print(res_copy, "res_copy")
            res = res_copy
            print(res, "res")
        return res

                

                        


        # def dfs(i):
        #     for perm in res:
        #         perm_copy = perm.copy()






# i = 2
# res = ((1,2) (2,1))
# perm = (1,2)
# perm_copy = (1,2), (1,2), (1,2)
# p = (1,2)
# 3,1,2 1,3,2 1,2,3