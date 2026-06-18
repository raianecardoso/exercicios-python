def resposta(numero1, numero2):
    while numero2 != 0:
        resultado = numero2
        numero2 = numero1 % numero2
        numero1 = numero2
        if numero2 != 0:
            resultado = numero2
    return(resultado)
