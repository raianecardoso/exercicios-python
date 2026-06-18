def resposta(n):
    a, b = 1, 1
    k = 1
    if n == 1 or n == 2:
        return(1)
    else:
        while k <= n-2:
            a, b = b, a + b
            k = k + 1
        return(b)
