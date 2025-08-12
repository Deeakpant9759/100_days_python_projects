def fibonacci(n):
    if n <= 1: return n
    prev , curr = 0,1
    counter = 1
    while counter <n:
        next = prev + curr
        prev,curr = curr,next
        counter += 1
    return curr
print(fibonacci(100))