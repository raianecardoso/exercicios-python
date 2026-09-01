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

mensagem_decodificada = resposta("GRIRSVEJ, IRZREV! MFTV TFETCLZL F TLIJF KIZCYR UVM GPKYFE", 17)

print(mensagem_decodificada)