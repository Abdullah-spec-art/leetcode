def twosum_sorted(nums,target):
    left=0
    right=len(nums)-1
    while nums:
        if nums[left]+nums[right]>target:
            right-=1
        elif nums[left]+nums[right]<target:
            left+=1
        else:
            return left, right



nums = [2, 7, 11, 15]
target = 9
print(twosum_sorted(nums,target))