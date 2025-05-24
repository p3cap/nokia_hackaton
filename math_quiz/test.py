import sympy as sp

# Változó definiálása
n = sp.symbols('n')

# Egyenlet definiálása
equation = n**2 - 2*n + 1

# Egyenlet megoldása
solutions = sp.solve(equation, n)

print("A megoldás(ok):", solutions)