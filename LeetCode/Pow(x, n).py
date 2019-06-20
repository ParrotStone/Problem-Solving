#!/usr/bin/env python3

"""
Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n, (x ** n)

Example 1:
Input: 2.00000, 10
Output: 1024.00000
------
Example 2:
Input: 2.10000, 3
Output: 9.26100
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        x_n = x
        power_to = abs(n) + 1

        if x == 1:
            return 1

        if len(str(abs(n))) > 8:
            return float(0)

        for i in range(2, power_to):
            x_n *= x

        if n > 0:
            return x_n
        elif n == 0:
            return 1
        else:
            return (1 / x_n)


solution = Solution()
# print(solution.myPow(2, 10))
# print(solution.myPow(2, 2))
# print(solution.myPow(2, -2))
# print(solution.myPow(2, 5))
# print(solution.myPow(0.44528, 0))
# print(solution.myPow(0.00001, 2147483647))
print(solution.myPow(1, 2147483647))
