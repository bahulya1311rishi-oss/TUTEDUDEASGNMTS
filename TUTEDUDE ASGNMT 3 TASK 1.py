
n = int(input(' Enter your number : '))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


result = factorial(n)

print( 'The factorial of', n, 'is', result)