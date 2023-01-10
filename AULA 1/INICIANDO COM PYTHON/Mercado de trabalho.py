#Foi lhe dada a missão de escolher uma ferramenta para desenvolver um protótipo para o cliente que fabrica peças automotivas. Uma opção é usar o Colab, pois nessa ferramenta você consegue implementar seu algoritmo usando a linguagem Python. Outra grande vantagem em utilizá-lo é o fato de ser on-line e não precisar de instalação. Uma vez pronto o protótipo, você pode enviar o link, tanto para seu gerente ver o resultado do seu trabalho, quanto para o cliente testar a solução.

#Uma vez decidida a ferramenta, é hora de começar a pensar na solução. Tudo que você tem de informação está em um gráfico, portanto é preciso interpretá-lo.

c = 200 # valor da constante

mes = input("Digite o mês que deseja saber o resultado: ") # Função para captura o mês que o cliente digitar
mes = int(mes) # Não esqueça de converter para numérico o valor captura pela função input()

r = c * mes # Equação do primeiro grau, também chamada função do primeiro grau ou de função linear.

print(f"A quantidade de peças para o mês {mes} será {r}") # Impressão do resultado usando string interpolada "f-strings" 