def palindrome(s):
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True     

print(palindrome("madam"))



def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n != largest:
            second_largest = n

    return second_largest if second_largest != float('-inf') else None      




# nums = [2, 7, 11, 15], target = 9 → True (because 2 + 7 = 9)
def two_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))











def second_largest(nums):
    largest=float("-inf")
    second_largest=float("-inf")
    for num in nums:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num<largest:
            second_largest=num
    return second_largest if second_largest!=float("inf") else None



nums = [2, 7, 11, 15]
print(second_largest(nums))