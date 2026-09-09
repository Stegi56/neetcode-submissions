class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]

            l, r = 0, 0
            for i in range(L, R + 1):
                if r >= len(right):
                    nums[i] = left[l]
                    l += 1
                elif l >= len(left):
                    nums[i] = right[r]
                    r += 1
                elif left[l] < right[r]:
                    nums[i] = left[l]
                    l += 1
                else:
                    nums[i] = right[r]
                    r += 1     

        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r ) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m , r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)