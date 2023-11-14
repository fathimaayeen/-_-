def fibonacci_generator():
    l = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

        l.append(a)
    return l


# Example: Generate the first 10 Fibonacci numbers
n = int(input("Enter input:"))
fibonacci_gen = fibonacci_generator()
print(*fibonacci_gen)