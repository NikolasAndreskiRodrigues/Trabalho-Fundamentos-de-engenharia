import json
from datetime import datetime

ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)

def adicionar_tarefa(tarefas):
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")
    prazo = input("Prazo (opcional, ex: 2025-05-07): ")
    tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'descricao': descricao,
        'prazo': prazo,
        'concluida': False,
        'criada_em': datetime.now().isoformat()
    }
    tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for t in tarefas:
        status = '✅' if t['concluida'] else '❌'
        print(f"{t['id']:03d} | {status} | {t['titulo']} (Prazo: {t['prazo']})")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        tid = int(input("ID da tarefa a marcar como concluída: "))
        for t in tarefas:
            if t['id'] == tid:
                t['concluida'] = True
                print("✔️ Tarefa marcada como concluída!")
                return
        print("⚠️ Tarefa não encontrada.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        tid = int(input("ID da tarefa a remover: "))
        for t in tarefas:
            if t['id'] == tid:
                tarefas.remove(t)
                print("🗑️ Tarefa removida.")
                return
        print("⚠️ Tarefa não encontrada.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            salvar_tarefas(tarefas)
            print("📁 Tarefas salvas. Saindo...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
