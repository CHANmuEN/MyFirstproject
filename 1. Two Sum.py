class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {} # key : diff , value :index
        for idx,num in enumerate(nums): #enumerate函數可以遍歷所有數值
            if diff.get(num,None)==None: #整數不在目標內
                diff[target-num] =idx
            else:
                return [diff[num] , idx]
