def resposta(peso):
    if peso > 50:
        excesso = (peso - 50)
        multa = excesso * 4
        return (excesso, multa)
    else:
        return (0, 0)

