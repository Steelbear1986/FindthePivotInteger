class Solution:
    def pivotInteger(self, n: int) -> int:
        ans=[i for i in range(n+1)]
        for i in range(len(ans)):
            if sum(ans[:i])==sum(ans[i+1:]):
                     return (ans[i])
        return -1