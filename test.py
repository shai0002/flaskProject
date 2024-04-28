a= [-7, 1, 5, 2, -4, 3, 0]
'''
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

A= [4, 1, 2, 2] 
A[0] = A[2] + A[3]
An index is said be an equilibrium index if Sum(left of elements) is equal to Sum(right of elements)
'''
import collections

def solution(a):

    for i in range(1, len(a)):
        sum_left = sum(a[:i])
        sum_right = sum(a[i+1:len(a)])
        if sum_left == sum_right:
            return i

    return -1
# a= [-7, 1, 5, 2, -4, 3, 0]
# print(solution(a))
# A= [4, 1, 2, 2]
# print(solution(A))


s = "aaaallleeewwaa"

ans = "a4l3e3w2a2"

def encode_string(s):

    count = 0
    ans = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            ans += s[i-1] + str(count)
            count = 0

    return ans
print(encode_string(s))
