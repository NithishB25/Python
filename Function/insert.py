def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))
obj = Solution()

print(obj.searchInsert(nums, target))