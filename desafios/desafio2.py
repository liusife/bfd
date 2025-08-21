# sistema de gestão de tarefas, usando while, append e listas! Revisar documentação
tarefas = []

while True:
    print("###################################")
    print("\nSistema de Gestão de Tarefas")
    print("\n1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    print("###################################")

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == '1':
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    elif escolha == '2':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Tarefas:")
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f"{idx}. {tarefa}")
    elif escolha == '3':
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            print("Tarefas:")
            for idx, tarefa in enumerate(tarefas, start=1):
                print(f"{idx}. {tarefa}")
            try:
                tarefa_idx = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                if 0 <= tarefa_idx < len(tarefas):
                    tarefa_removida = tarefas.pop(tarefa_idx)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif escolha == '4':
        print("Saindo do sistema. Até logo!")
        break