#!/usr/bin/env python3


# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         dividend_temp = abs(dividend)
#         absolute_divisor = abs(divisor)
#         counter = 0

#         if abs(divisor) == 1 and abs(dividend) == (2 ** 31):
#             result = dividend * divisor
#             return result if result < 0 else result - 1

#         if abs(divisor) == 1:
#             return (dividend * divisor)

#         while dividend_temp >= absolute_divisor:
#             dividend_temp -= absolute_divisor
#             counter += 1

#         if (divisor < 0 and dividend < 0) or (divisor > 0 and dividend > 0):
#             return counter

#         return (counter * -1)


# solution = Solution()
# # print(solution.divide(10, 3))
# # print(solution.divide(7, -3))
# # print(solution.divide(5, 2))
# # print(solution.divide(15, 2))
# # print(solution.divide(-7, 3))
# # print(solution.divide(-7, -3))
# # print(solution.divide(7, 3))
# # print(solution.divide(1, 2147483648))
# # print(solution.divide(-2147483648, -1))
# # print(solution.divide(-2147483648, 1))
# # print(solution.divide(2147483648, 1))
# # print(solution.divide(2147483648, -1))
# # print(solution.divide(-2147483648, -1))
# # print(solution.divide(-2147483648, 1))
# print(solution.divide((2 ** 31) -1, 2))


# """
# print(solution.divide(-2147483648, -1))

# """

# Main functionality first
# Negativity thingie
# remove asterisks from your code


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if abs(divisor) == 1 and abs(dividend) == (2 ** 31):
            result = dividend * divisor
            return result if result < 0 else result - 1

        if abs(divisor) == 1:
            return (dividend * divisor)

        if abs(dividend) == abs(divisor):
            if (divisor < 0 and dividend < 0) or (divisor > 0 and dividend > 0):
                pass

        divisor_temp = abs(divisor)
        counter = 0
        is_even = False
        while divisor_temp >= 0:
            divisor_temp -= 2
            if divisor_temp == 0:
                is_even = True
                break
            counter += 1

        result = (abs(dividend) >> counter)
        if is_even:
            return -result if divisor < 0 else result
        else:
            return -(result + 1) if divisor < 0 else result + 1

        # if (divisor < 0 and dividend < 0) or (divisor > 0 and dividend > 0):
        #     return counter

        # return (counter * -1)


solution = Solution()
# print(solution.divide(10, 3))

# 1010
# 1010
# 0011
# 1000
# print(solution.divide(-50, 8))
print(solution.divide(2147483647, 3))
# print(solution.divide(2147483648, 1))
# print(solution.divide(-2147483647, -2))
# print(solution.divide(-2147483647, -3))
# print(solution.divide(-10, -3))

# print(result)
