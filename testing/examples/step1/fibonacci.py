from pprint import pprint

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == 'main':
    pprint(fibonacci(5))
