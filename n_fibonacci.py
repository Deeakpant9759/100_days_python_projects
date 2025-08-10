def fibonacci_Sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    number = fibonacci_Sol(n-1) + fibonacci_Sol(n-2)
    return number
    
print(fibonacci_Sol(50))
