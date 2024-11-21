# Solicitar ao usuário que insira dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Calcular o quociente inteiro e o resto da divisão
quociente = numero1 // numero2
resto = numero1 % numero2

# Exibir os resultados
print(f"O quociente inteiro da divisão de {numero1} por {numero2} é: {quociente}")
print(f"O resto da divisão de {numero1} por {numero2} é: {resto}")
