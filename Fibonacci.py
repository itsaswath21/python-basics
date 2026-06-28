def fibonacci(n):
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


num = int(input("Enter number of terms: "))

if num <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Series:", fibonacci(num))
