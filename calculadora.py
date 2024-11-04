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
