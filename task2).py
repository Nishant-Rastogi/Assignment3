import math
def square_root(n):
    res1 = math.sqrt(n)
    return res1
def log(n):
    res2 = math.log(n)
    return res2
def Sine(n):
    res3 =math.sin(math.radians(n))
    return res3
val = int(input("Enter a number: "))
out1 = square_root(val)
out2 = log(val)
out3 = Sine(val)
print(f"Square root: {out1}")
print(f"Logarithm: {out2}")
print(f"Sine: {out3}")

