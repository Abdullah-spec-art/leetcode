def isPalindrome(x):
    if x < 0 or (x % 10==0 and x!=0):
        return False
    reverse=0
    while x>reverse:
        num=x%10
        reverse=reverse*10+num
        x//=10
    return x==reverse or x==reverse//10


x=121
print(isPalindrome(x))