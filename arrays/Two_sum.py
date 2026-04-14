def twosum(nums,target):
    dic={}
    for index, num in enumerate(nums):
        diff=target-num
        if diff in dic:
            return [dic[diff], index]
        dic[num]=index

nums = [2, 7, 11, 15]
target = 9
print(twosum(nums,target))