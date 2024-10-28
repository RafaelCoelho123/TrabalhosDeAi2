# Inicializa uma lista para o histórico de operações
historico = []

while True:
    # Solicita o primeiro número ou uma opção para sair
    entrada_x = input("Escolhe 1 número (ou digite 'sair' para terminar): ")
    if entrada_x.lower() == 'sair':
        break  # Sai do loop se o usuário digitar 'sair'

    # Tenta converter a entrada para um inteiro
    try:
        x = int(entrada_x)
    except ValueError:
        print("Por favor, insira um número válido.")
        continue  # Volta para o início do loop

    # Solicita o segundo número
    y = int(input("Escolhe outro número: "))
    op = input("Escolhe uma operação (+, -, /, *, historico): ")

    # Calcula o resultado com base na operação escolhida
    if op == "+":
        resultado = x + y
        historico.append(f"{x} + {y} = {resultado}")
    elif op == "-":
        resultado = x - y
        historico.append(f"{x} - {y} = {resultado}")
    elif op == "*":
        resultado = x * y
        historico.append(f"{x} * {y} = {resultado}")
    elif op == "/":
        if y != 0:
            resultado = x / y
            historico.append(f"{x} / {y} = {resultado}")
        else:
            resultado = "Erro: Divisão por zero."
            print(resultado)
            continue  # Continua para a próxima iteração
    elif op.lower() == "historico":
        print("Histórico das últimas operações:")
        for operacao in historico[-5:]:
            print(operacao)
        continue  # Volta para o início do loop
    else:
        print("Operação inválida.")
        continue  # Volta para o início do loop

    # Exibe o resultado
    print("O resultado da tua conta dá:", resultado)

    # Mantendo o histórico limitado a 5 operações
    if len(historico) > 5:
        historico.pop(0)  # Remove a operação mais antiga