class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            elif total > target:
                j = j - 1
            else:
                i = i + 1

        raise Exception("No solution")