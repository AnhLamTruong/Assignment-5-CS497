class Solution(object):
    def removeInvalidParentheses(self, string):  ## method to remove invalid parenthesis
       
        def calculate(string):
            leftindex = 0
            rightindex = 0
            for c in string:
                if c == '(':
                    leftindex += 1
                elif c == ')':
                    if leftindex == 0:
                        rightindex += 1
                    else:
                        leftindex -= 1
            return leftindex + rightindex
        
        def dfs(string):  ## using depth first to solve
            n = calculate(string)
            if n == 0:
                return [string]
            ans = []
            for i in range(len(string)):
                if string[i] in ['(', ')']:
                    sos = string[:i] + string[i + 1:]
                    if sos not in visited and calculate(sos) < n:
                        visited.add(sos)
                        ans.extend(dfs(sos))
            return ans
            
        visited = set([string]) ## passing set of the string to  visited array
        return dfs(string)
        
        
object=Solution()   ## making the object of the class   
print(object.removeInvalidParentheses("(a)())()"))
print(object.removeInvalidParentheses("()())()"))
print(object.removeInvalidParentheses(")("))
