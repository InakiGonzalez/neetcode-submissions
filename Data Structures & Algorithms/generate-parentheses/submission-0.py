class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(op,cl,string):
            if op == n and cl == n:
                res.append(string)
                return
            if op < n: 
                backtrack(op +1, cl, string+"(")
            if cl < op:
                backtrack(op, cl+1, string + ")")

        backtrack(0,0,"")
        return res

        