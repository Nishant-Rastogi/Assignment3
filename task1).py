def fact_rect(num):
    if num <= 1:
        return 1
    else:
        factorial = num * fact_rect(num-1)
        return factorial
n = int(input("Enter a number: "))
fact = fact_rect(n)
print(f"Factorial of {n} is {fact}")