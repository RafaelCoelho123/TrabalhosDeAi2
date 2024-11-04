# Configurações e manipulação do histórico

HISTORICO_MAX = 5  # Constante para o número máximo de operações no histórico
historico = []  # Lista para armazenar o histórico das operações

def adicionar_historico(operacao):
    """Adiciona uma operação ao histórico, removendo a mais antiga se necessário."""
    if len(historico) >= HISTORICO_MAX:
        historico.pop(0)  # Remove a operação mais antiga
    historico.append(operacao)

def mostrar_historico():
    """Mostra o histórico das últimas operações realizadas."""
    if historico:
        print("\nHistórico das últimas operações:")
        for i, operacao in enumerate(historico, 1):
            print(f"{i}. {operacao}")
    else:
        print("\nNenhuma operação no histórico ainda.")
