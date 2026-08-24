---
Tags: Strings, Métodos de String, Laços de Repetição (for), Estruturas Condicionais (if), Funções
Nível: Iniciante
---
# DESAFIO FINAL

## Objetivo
 
Praticar manipulação de strings implementando a **Cifra de César** para decodificar uma mensagem secreta.
 
## Contexto
 
A Cifra de César desloca cada letra do alfabeto um número fixo de posições. Com chave `3`, `A` vira `D`, `B` vira `E`, e assim por diante. Para decodificar, o processo é inverso: desloca-se as letras para trás, na mesma quantidade.
 
Você recebeu, no comentário do Issue, uma **mensagem codificada** e uma **chave** (um número inteiro). Sua tarefa é escrever o código que reverte a cifra e recupera a mensagem original.
 
## Especificação
 
Abra o arquivo `desafio_final/main.py` e localize a função `resposta`.
 
A função espera receber dois parâmetros: `mensagem`, uma string com o texto codificado, e `chave`, um número inteiro com a quantidade de posições do deslocamento.
 
Passos:
 
1. Percorra a  `mensagem`.
2. Se o caractere for uma letra (`.isalpha()`), aplique a fórmula de decodificação da Cifra de César; se não for (espaço, vírgula, `!`), mantenha como está.
3. Concatene o resultado numa nova string e retorne-a com `return` ao final.

### Dica: 
 
Utilize `posicao = ord(char) - ord("A")` para obter a posição da letra no alfabeto, considerando `A = 0`, `B = 1`, ..., `Z = 25`.

```python
char = "B"

posicao = ord(char) - ord("A")
print(posicao)  # 1

posicao = (posicao - 5) % 26
print(posicao)  # 22

# converta o número de volta para letra
nova_letra = chr(posicao + ord("A"))
```

Nesse exemplo, o `% 26` faz o deslocamento "dar a volta" no alfabeto, transformando a posição `-4` em `22`.
 
### Hora de decifrar sua mensagem secreta:
 
Se os testes passaram, seu decodificador está pronto, chegou a hora de usá-lo no desafio de verdade: decodificar a mensagem que você recebeu na Issue.
 
No final do `main.py`, fora da função, chame a `resposta` com os valores reais:
 
```python
mensagem_decodificada = resposta(mensagem, chave)
print(mensagem_decodificada)
```
 
Rode o arquivo, tire um print do terminal mostrando a frase decodificada e cole esse print como comentário na Issue do desafio.
