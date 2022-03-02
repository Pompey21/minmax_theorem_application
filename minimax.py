from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

x1 = solver.NumVar(0, solver.infinity(), 'x1')
x2 = solver.NumVar(0, solver.infinity(), 'x1')
x3 = solver.NumVar(0, solver.infinity(), 'x1')
x4 = solver.NumVar(0, solver.infinity(), 'x1')
x5 = solver.NumVar(0, solver.infinity(), 'x1')


print('Number of variables =', solver.NumVariables())