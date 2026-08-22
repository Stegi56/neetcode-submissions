class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find rotation point
        #treat before/ after point as sepperate arrays
        # search in the right one based on if range is <> than target

        l, r = 0, len(nums) - 1

        while l < r:
            cur = (l + r) // 2
            if nums[cur] > nums[r]:
                l = cur + 1
            else:
                r = cur

        mid = l

        if mid == 0 or target <= nums[-1]:
            r = len(nums) - 1
        else:
            l, r = 0, mid - 1

        while l <= r:
            cur = (l + r) // 2
            if nums[cur] == target:
                return cur
            elif nums[cur] < target:
                l = cur + 1
            else:
                r = cur - 1

        return -1
            