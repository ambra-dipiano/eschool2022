from logging import warning

def fibonacci(n):
    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')
    if n > 40:
        warning(f'This test is terrible you should keep n < 40, got {n}')
    # rest unchanged
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
