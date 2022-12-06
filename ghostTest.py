def backtrack(self,app):
    targetR, targetC = app.pacman.r, app.pacman.c
    solution = self.backtrackHelper(app,[],[],targetR,targetC)
    return solution

def backtrackHelper(self,app,solution,dirs,targetR,targetC):
    if solution[-1] == (targetR,targetC):
        return dirs[-1]
    else:
        for i in range(len(self.directions)):
            r,c = 0,0
            if len(solution) == 0:
                r = self.r
                c = self.c
            else:
                r,c = solution[-1]
            if self.isLegal(r,c,app,self.directions[i]):
                dr,dc = self.directionChanges[i]
                solution.append((r+dr,c+dc))
                dirs.append(self.directions[i])
                newSol = self.backtrackHelper(app,solution,dirs,targetR,targetC)
                if newSol != None:
                    return newSol
                else:
                    solution.pop()
                    dirs.pop()
        return None