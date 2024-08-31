def is_fibonacci(n):
    # Função para verificar se um número está na sequência de Fibonacci
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def main():
    numero = int(input("Digite um número: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
