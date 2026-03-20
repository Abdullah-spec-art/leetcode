def conainer_with_more_water(arr):
    max_water=0
    left=0
    right=len(arr)-1
    while left<right:
        width=right-left
        current_height=min(arr[left],arr[right])
        current_water=width*current_height
        max_water=max(max_water,current_water)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
            
    return max_water


arr=[1, 8, 6, 2, 5, 4, 8, 3, 7]
print(conainer_with_more_water(arr))