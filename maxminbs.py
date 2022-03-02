from gekko import GEKKO

m = GEKKO(remote=False)
x1,x2,x3,x4,x5,V = m.Array(m.Var,6)
m.Minimize(V)
m.Equations([x1>=0,x2>=0,x3>=0,x4>=0,x5>=0,V>=0])
m.Equation(x1+x2+x3+x4+x5==1)
m.Equations([V-3*x1-3*x2-9*x3-6*x4-2*x5 >= 0,
             V-7*x1-8*x2-4*x3-5*x4-3*x5 >= 0,
             V-1*x1-2*x2-5*x3-6*x4-4*x5 >= 0,
             V-1*x1-4*x2-4*x3-5*x4-8*x5 >= 0,
             V-4*x1-7*x2-7*x3-8*x4-3*x5 >= 0])
m.solve()
print('x1: ',x1.value[0])
print('x2: ',x2.value[0])
print('x3: ',x3.value[0])
print('x4: ',x4.value[0])
print('x5: ',x5.value[0])
print('V:  ',V.value[0])