# A função abaixo irá verifficar se o número informado pertence ao fibonacci
def pertence_a_fibonacci(n):
    if n < 0:
        return False
    
    # A função abaixo irá gerar números de Fibonacci de acordo com o fornecido
    def gerar_fibonacci(maximo):
        fibonacci = [0, 1] # Lista onde mostra os números que inicia a Fibonacci
        while True:
            numero_seguinte = fibonacci[-1] + fibonacci[-2] 
            if numero_seguinte > maximo:
                break
            fibonacci.append(numero_seguinte)
        return fibonacci
    
    # Gera a sequência de Fibonacci até o número informado
    fib_sequence = gerar_fibonacci(n)
    
    # Verifica se o número informado está na sequência gerada
    return n in fib_sequence

# Solicitando um número ao usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando e exibindo o resultado
if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")