def fib(n, memo={}):
    if n in memo:
        return memo[n]
    elif n in [1,2]:
        return 1
    else:
        memo[n] = fib(n - 1) + fib(n-2)

    return memo[n]

def fib_rec(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
