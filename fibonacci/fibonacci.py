
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Agora você pode chamar a função com o valor de n desejado
  # Substitua pelo número desejado
n = int(input("Digite o valor que queria descobrir "))
resultado = fibonacci(n)
print(f"O {n}-ésimo termo da sequência de Fibonacci é {resultado}")