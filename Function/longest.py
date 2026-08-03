from typing import List

strs = ["flower", "flow", "flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(Prefix):
                Prefix = Prefix[:-1]

                if Prefix == "":
                    return ""

        return Prefix

obj = Solution()
print(obj.longestCommonPrefix(strs))