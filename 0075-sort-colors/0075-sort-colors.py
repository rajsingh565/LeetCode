class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        last_zero = 0
        r = len(nums)-1
        while l <= r:
            if nums[l] == 0:
                if nums[last_zero] != 0:
                    nums[l], nums[last_zero] = nums[last_zero], nums[l]
                last_zero+=1
                l+=1
                continue
            if nums[r] == 2:
                r-=1
                continue
            if nums[l] == 1 and nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                if nums[l] == 0 and nums[last_zero] != 0:
                    nums[l], nums[last_zero] = nums[last_zero], nums[l]
                last_zero += 1
            if nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                if nums[l] == 0:
                    if nums[last_zero] != 0:
                        nums[l], nums[last_zero] = nums[last_zero], nums[l]
                    last_zero += 1
                r-=1
            l+=1
            