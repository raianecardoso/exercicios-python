def resposta(mensagem, chave):
    resultado = ""

    for char in mensagem:
        if char.isalpha():
            posicao = ord(char) - ord("A")
            posicao = (posicao - chave) % 26
            nova_letra = chr(posicao + ord("A"))
            resultado += nova_letra
        else:
            resultado += char
    return resultado

mensagem_decodificada = resposta("MXOXYBKP, ! SLZB ZLKZIRFR L ZROPL QOFIEX ABS MVQELK", 23)

print(mensagem_decodificada)