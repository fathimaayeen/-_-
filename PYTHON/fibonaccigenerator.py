def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Enter Numer:\n"))
fibonacci_gen = fibonacci()
fibonacci_seq = [next(fibonacci_gen) for _ in range(n)]
print(*fibonacci_seq)
