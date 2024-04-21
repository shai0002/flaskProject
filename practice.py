def removeDuplicates(nums) -> int:
    '''left = updates when right pointer identifies a unique num and assigns the element at right position to left
    right = position of unique num, and updates when it assigns right pointer element to left'''
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    nums[:] = nums[:left]
    return len(nums)
# nums = [0,0,1,1,1,2,2,3,3,4]
# ans = removeDuplicates(nums)
# print(ans)

nums = [7,1,5,3,6,4]
def maxProfit(prices) -> int:
    '''returns the max profit'''
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    for i in range(0, len(prices)-1):
        if prices[i] < prices[i + 1]:
            max_profit += prices[i + 1] - prices[i]
    return max_profit
#print(maxProfit(nums))




