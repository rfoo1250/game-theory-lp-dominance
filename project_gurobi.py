#!/usr/bin/env python
import gurobipy as gp
from gurobipy import GRB
import numpy as np

def find_mixed_dominator(A, i, tol=1e-6):
    n = A.shape[0]
    model = gp.Model()
    model.Params.OutputFlag = 0
    P = model.addVars([k for k in range(n) if k != i], lb=0, ub=1, name="p")
    eps = model.addVar(lb=0, name="eps")
    model.addConstr(sum(P[k] for k in P) == 1)
    for j in range(n):
        model.addConstr(
            sum(P[k] * A[k, j] for k in P) >= A[i, j] + eps
        )
    model.setObjective(eps, GRB.MAXIMIZE)
    model.optimize()
    if model.Status == GRB.OPTIMAL and eps.X > tol:
        return True, {k: P[k].X for k in P}, eps.X
    return False, None, None

def iterative_elimination(A):
    rem = list(range(A.shape[0]))
    while True:
        for idx in rem:
            A_sub = A[np.ix_(rem, rem)]
            pos = rem.index(idx)
            dominated, _, _ = find_mixed_dominator(A_sub, pos)
            if dominated:
                rem.remove(idx)
                break
        else:
            break
    return rem

if __name__ == "__main__":
    print("Gurobi version:", gp.gurobi.version())
    A = np.array([
        [3, 0, 2, 1],
        [0, 1, 2, 2],
        [1, 0, 1, 1],
        [2, 2, 2, 2]
    ], float)
    print("Surviving strategies:", iterative_elimination(A))
