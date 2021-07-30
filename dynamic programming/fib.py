def fib(n, memo={}):
    if n in memo:
        return memo[n]
    elif n in [1,2]:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n-2, memo)

    return memo[n]

def fib_rec(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(500))
