class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        maps={}
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                prod=nums[i]*nums[j]
                if prod in maps:
                    maps[prod]+=1
                else:
                    maps[prod]=1
        ans=0
        for ele in maps:
            if maps[ele]>1:
                ans+=(maps[ele]*(maps[ele]-1))*8//2
        return ans