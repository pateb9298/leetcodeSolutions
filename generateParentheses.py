class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTrack(path, open, close):
            if open==n and close==n:
                res.append(path)
                return

            if open<n:
                backTrack(path + "(", open+1, close)

            if close<open:
                backTrack(path + ")", open, close+1)
            

        backTrack("", 0, 0)
        return res
