def fibonacci(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n
n = int(input('Digite um número: '))
if fibonacci(n):
    print(f'O número {n} pertence à sequência de Fibonacci.')
else:
    print(f'O número {n} não pertence à sequência de Fibonacci.')