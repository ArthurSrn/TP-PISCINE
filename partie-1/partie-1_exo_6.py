# On souhaite écrire une fonction qui accepte en argument un terme de la suite de Fibonacci(n) et un nombre(m), et renvoie la somme des termes n à n+m dans la suite de Fibonacci.


def sum_fibonacci(n, m):
    a, b = 0, 1
    fib_sum = 0
    for i in range(n+m):
        if i >= n:
            fib_sum += a
        a, b = b, a+b
    return fib_sum


print(sum_fibonacci(5, 10))
