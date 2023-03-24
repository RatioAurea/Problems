def howSum(targetSum, numbers, memo = None):
    if memo == None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return remainderResult

    memo[targetSum] = None
    return None

print(howSum(15, [2,3]))
print(howSum(875, [23, 21, 28]))
