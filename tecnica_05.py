# Definindo a string (pode ser alterada ou recebida como input)
texto = input("Digite a string que deseja inverter: ")

# Inicializando uma variável para armazenar a string invertida
texto_invertido = ""

# O loop for percorre a string do último caractere (len(texto) - 1)
# até o primeiro, adicionando cada caractere à variável texto_invertido.
for string in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[string]

# Exibindo o resultado
print(f"String invertida: {texto_invertido}")