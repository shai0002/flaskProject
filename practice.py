from typing import Optional


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

import collections
import logging
class Solution:
    def findFarmland(land):
        # farmland coardinates of topleft 1 and bottom right 1
        # for every grp of island we need to return the starting and ending '1' cordinate
        rows = len(land)
        cols = len(land[0])
        visited = set()
        res = []
        q = collections.deque()
        i = 0

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))
            min_r, min_c, max_r, max_c = r, c, r, c  # intializing the group start and end's coordinate
            while q:
                row, col = q.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and (r, c) not in visited
                            and land[r][c] == 1):
                        visited.add((r, c))
                        q.append((r, c))
                        # find the min and max row col cordinated we've seen so far and reassign the coordinates
                        min_r = min(min_r, r)
                        min_c = min(min_c, c)
                        max_r = max(max_r, r)
                        max_c = max(max_c, c)
            return [min_r, min_c, max_r, max_c]

        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1 and (row, col) not in visited:
                    farmland = bfs(row, col)
                    res.append(farmland)
        print(res)
        return res
# Solution.findFarmland([[1,0,0],[0,1,1],[0,1,1]])

def reverse(nums):
    res = []
    for i in range(len(nums)-1, -1, -1):
        res.append(nums[i])
    print(res)
    return res
reverse(nums)

arr = [1, 5, 7, -1, 5]
sum = 6

def find_pairs(arr, sum):
    s_map = {}
    res = []
    for i, num in enumerate(arr):
        if (sum-num) in s_map:
            res.append([s_map[sum-num], i])
        s_map[num] = i
    print(res)
    return res
find_pairs(arr, sum)
i = [i for i in range(-50,51)]
print(i)
i = filter(lambda x: x%2==0, range(0,11)) # filter obj
print([j for j in i])



import numpy as np
n_arr = np.array([1,2,3,4,5])
n_arr = np.append(n_arr, "hi")
print(n_arr)

#================================================
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "+":
                result += sign * num
                num = 0
                sign = 1
            elif char == "-":
                result += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                result *= stack.pop()  # Pop the sign.
                result += stack.pop()  # Pop the preceding result.

        result += sign * num
        return result


# Example usage:
solution = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
result = solution.calculate(s)
print(result)  # Output: 23

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        curr_pos = new_list
        carry_fwd = 0
        while l1 or l2 or carry_fwd:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry_fwd
            carry_fwd = val // 10
            val = val % 10
            # insert the summed value
            curr_pos.next = ListNode(val)

            # Update the pointers l1 & l2
            curr_pos = curr_pos.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new_list.next