# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:52:51 2020

@author: Hageresebb
"""

#Q2.3 second
import cvxpy as cp
x1 = cp.Variable()
x2 = cp.Variable()
p = cp.Parameter()
#adding parameter here helps us change the value of a constant in a 
#problem without reconstructing the entire problem
log=cp.log(x1+x2-4+p)
#for t in range(1 , 1000) 
t=100

#log=log/t
obj = cp.Minimize((x1-2)**2 + 3*x2-log/t)
constraints= None
# Form and solve problem.
prob = cp.Problem(obj, constraints)
# Returns the optimal value.
# Solve with ECOS.
p.value = 2.0
prob.solve(solver=cp.ECOS)
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal value", obj.value)
print("optimal var", x1.value, x2.value)