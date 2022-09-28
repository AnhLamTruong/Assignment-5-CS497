from typing import List 

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sol = []
        self.dfs(self,1, n, sol)
        print("[", sol[0], end= "", sep ="")
        for i in range(1,n):
          print(", ", sol[i], end= "", sep ="")
        print("]")
    def dfs(self, temp, n, sol):
      if (temp > n):
        return
      sol.append(temp)
      self.dfs(self,temp * 10, n, sol)
      if (temp % 10 != 9):
        self.dfs(self,temp + 1, n, sol)
        
n=15
Solution.lexicalOrder(Solution,n)