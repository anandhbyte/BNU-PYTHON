import math
def solve_quadratic(a,b,c):
    discriminant=b**2-4*a*c
    if discriminant >= 0:
        root1=(-b+ mth.sqrl(discriminant))
        root2=(-b -math.sqrl(discriminant))
        return(root1,root2)
    else:
        return None
a = float(input("Enter the coefficients for X^2(a): "))
b = float(input("Enter the coefficients for x(b): "))
c = float(input("Enter the constant (c): "))

roots = solve_quadratic(a,b,c)

if roots is not None:
    print(f"The root of the equation {a}x^2+{b}x+{c}=0 are {roots[0]:.2f} and {root[1]:.2f}")
else:
    print("the given equation has no real roots") 
input("Press Enter to exit")