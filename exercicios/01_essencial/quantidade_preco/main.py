import math

def resposta(area):
    n_latas = (math.ceil(area / (3 * 18)))
    preço = n_latas * 80.0
    return (n_latas, preço)

