def dailyTemperatures(temps):
    stack=[]
    result=[0]*len(temps)

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result
 
print(dailyTemperatures([73,74,75,71,69,72,76,73]))