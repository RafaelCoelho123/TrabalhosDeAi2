# Constante para o número máximo de operações no histórico
HISTORICO_MAX = 5

# Lista para armazenar o histórico das operações
historico = []

# Função para adicionar operação ao histórico
def adicionar_historico(operacao):
    if len(historico) >= HISTORICO_MAX:
        historico.pop(0)  # Remove a operação mais antiga
    historico.append(operacao)

# Função para mostrar o histórico das últimas 5 operações
def mostrar_historico():
    if historico:
        print("\nHistórico das últimas operações:")
        for i, operacao in enumerate(historico, 1):
            print(f"{i}. {operacao}")
    else:
        print("\nNenhuma operação no histórico ainda.")
# Função principal da calculadora

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        # Condição de saída
        if opcao == '6':
            print("Saindo da calculadora.")
            break

        # Opção para mostrar o histórico
        elif opcao == '5':
            mostrar_historico()
            continue
# Função principal da calculadora com entrada de números

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        # Condição de saída
        if opcao == '6':
            print("Saindo da calculadora.")
            break

        # Opção para mostrar o histórico
        elif opcao == '5':
            mostrar_historico()
            continue

        # Solicita os números para as operações
        elif opcao in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Digite o primeiro número inteiro: "))
                num2 = int(input("Digite o segundo número inteiro: "))
            except ValueError:
                print("Por favor, digite números inteiros válidos.")
                continue
# Função principal da calculadora completa com operações

def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        # Condição de saída
        if opcao == '6':
            print("Saindo da calculadora.")
            break

        # Opção para mostrar o histórico
        elif opcao == '5':
            mostrar_historico()
            continue

        # Solicita os números para as operações
        elif opcao in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Digite o primeiro número inteiro: "))
                num2 = int(input("Digite o segundo número inteiro: "))
            except ValueError:
                print("Por favor, digite números inteiros válidos.")
                continue

            # Realiza a operação com base na escolha do usuário
            if opcao == '1':
                resultado = num1 + num2
                operacao = f"{num1} + {num2} = {resultado}"
            elif opcao == '2':
                resultado = num1 - num2
                operacao = f"{num1} - {num2} = {resultado}"
            elif opcao == '3':
                resultado = num1 * num2
                operacao = f"{num1} * {num2} = {resultado}"
            elif opcao == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não permitida.")
                    continue
                resultado = num1 // num2  # Divisão inteira
                operacao = f"{num1} // {num2} = {resultado}"

            # Mostra o resultado da operação
            print("Resultado:", operacao)

            # Adiciona a operação ao histórico
            adicionar_historico(operacao)

        else:
            print("Opção inválida. Tente novamente.")

# Inicia a calculadora
calculadora()
