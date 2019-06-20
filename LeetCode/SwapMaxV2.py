#!/usr/bin/env python3


class Solution:
    def maximum_swap(self, num: int) -> int:
        digit_list = list(str(num))
        i = 0
        result = ''
        swapped = False

        while not swapped and i < len(digit_list):
            mx_index = str(num).rfind(max(digit_list[i:]))
            if digit_list[i] < digit_list[mx_index]:
                digit_list[i], digit_list[mx_index] = digit_list[mx_index], digit_list[i]
                swapped = True
            else:
                i += 1

        for i in digit_list:
            result += i

        return int(result)


solution = Solution()
print(solution.maximum_swap(234))  # 432
print(solution.maximum_swap(2736))  # 7236
print(solution.maximum_swap(9973))  # 9973
print(solution.maximum_swap(9783))  # 9873
print(solution.maximum_swap(98368))  # 98863
print(solution.maximum_swap(1993))  # 9913
print(solution.maximum_swap(3991))  # 9931
print(solution.maximum_swap(1919))  # 9911
print(solution.maximum_swap(1191989))  # 9191981
