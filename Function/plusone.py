class Solution:
 def plusOne(self, digits: list[int]) -> list[int]:

        num = ""

        for i in digits:
            num += str(i)

        num = int(num) + 1

        result = []

        for i in str(num):
            result.append(int(i))

        return result


digits = list(map(int, input("Enter digits separated by space: ").split()))

obj = Solution()
print(obj.plusOne(digits))
