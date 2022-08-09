from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:   # noqa
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()


if __name__ == '__main__':
    input_array = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(input_array)
    assert input_array == [1, 0, 0, 2, 3, 0, 0, 4]

    input_array = [1, 2, 3]
    Solution().duplicateZeros(input_array)
    assert input_array == [1, 2, 3]

    input_array = [0]
    Solution().duplicateZeros(input_array)
    assert input_array == [0]
