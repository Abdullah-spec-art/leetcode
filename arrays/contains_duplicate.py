s=set()
def containsDuplicate(nums):
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))

#Another way 

def contains_duplicate(nums):
    return len(nums) != len(set(nums))