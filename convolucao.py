# Importação da biblioteca matplotlib
import matplotlib.pyplot as plt


def input_vector(prompt):
    while True:
        try:
            user_input = input(prompt)
            vector = [float(num_str) for num_str in user_input.split()]
            return vector
        except ValueError:
            print(
                "Entrada inválida. Por favor, insira um vetor válido (por exemplo, '1 2 3')."
            )


def manual_convolve(x, y):
    # Criando um vetor para armazenar os resultados da convolução
    result = [0] * (len(x) + len(y) - 1)

    # Loop aninhado para calcular a convolução dos vetores x e y
    for i in range(len(x)):
        for j in range(len(y)):
            result[i + j] += x[i] * y[j]

    return result


# Solicitação dos vetores x e y do usuário usando a função input_vector
x = input_vector("Insira o vetor x (por exemplo, '1 2 3'): ")
y = input_vector("Insira o vetor y (por exemplo, '4 5 6'): ")

# Realiza a convolução dos vetores x e y usando a função manual_convolve
conv = manual_convolve(x, y)

# Cria uma nova figura com tamanho especificado
plt.figure(figsize=(8, 4))

# Plota o resultado da convolução como pontos ('o')
plt.plot(conv, "o")

# Configura o título e os rótulos dos eixos do gráfico
plt.title("Convolução dos vetores x e y")
plt.xlabel("Índice")
plt.ylabel("Valor")

# Desenha linhas de eixo na posição 0 do gráfico com espessura de 2.5
plt.axhline(0, color="black", linewidth=2.5)
plt.axvline(0, color="black", linewidth=2.5)

# Para cada valor no vetor de convolução, desenha uma linha vertical do eixo x (posição 0) até o valor do ponto
for i, v in enumerate(conv):
    plt.vlines(i, 0, v, color="blue")

# Adiciona uma grade ao gráfico para melhor visualização
plt.grid(True)

# Mostra o gráfico
plt.show()
