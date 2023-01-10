#Junto com o comando for, podemos usar a função enumerate() para retornar à posição de cada item, dentro da sequência. Considerando o exemplo dado, no qual atribuímos a variável "nome" o valor de "Guido", "G" ocupa a posição 0 na sequência, "u" ocupa a posição 1, "i" a posição 2, e assim por diante. A função enumerate() recebe como parâmetro a sequência e retorna a posição. Para que possamos capturar tanto a posição quanto o valor, vamos precisar usar duas variáveis de controle. Observe o código a seguir, veja que a variável "i" é usada para capturar a posição e a variável "c" cada caracter da palavra.

nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")