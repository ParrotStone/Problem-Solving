#!/usr/bin/env python3


class Solution:
    def maximumSwap(self, num: int) -> int:

        digit_list = list(str(num))

        max_num = num
        for i in range(0, len(str(num))):
            for j in range(i + 1, len(str(num))):
                # Do the swap down here...
                digit_list[i], digit_list[j] = digit_list[j], digit_list[i]

                if list(str(max_num)) < digit_list:
                    foo = ''
                    for item in digit_list:
                        foo += item

                    max_num = int(foo)

                digit_list[i], digit_list[j] = digit_list[j], digit_list[i]

        return max_num


solution = Solution()
print(solution.maximumSwap(234))
print(solution.maximumSwap(98368))
print(solution.maximumSwap(9873))
print(solution.maximumSwap(1993))
print(solution.maximumSwap(3991))
