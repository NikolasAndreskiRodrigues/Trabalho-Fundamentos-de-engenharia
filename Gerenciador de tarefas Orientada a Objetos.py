import json
from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, descricao, prazo, concluida=False, criada_em=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prazo = prazo
        self.concluida = concluida
        self.criada_em = criada_em or datetime.now().isoformat()

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prazo': self.prazo,
            'concluida': self.concluida,
            'criada_em': self.criada_em
        }

    @staticmethod
    def from_dict(data):
        return Tarefa(**data)


class GerenciadorTarefas:
    ARQUIVO = 'tarefas.json'

    def __init__(self):
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        try:
            with open(self.ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [Tarefa.from_dict(t) for t in dados]
        except FileNotFoundError:
            return []

    def salvar_tarefas(self):
        with open(self.ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=2, ensure_ascii=False)

    def adicionar_tarefa(self):
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição: ")
        prazo = input("Prazo (opcional, ex: 2025-05-07): ")
        nova_tarefa = Tarefa(
            id=len(self.tarefas) + 1,
            titulo=titulo,
            descricao=descricao,
            prazo=prazo
        )
        self.tarefas.append(nova_tarefa)
        print("✅ Tarefa adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for t in self.tarefas:
            status = '✅' if t.concluida else '❌'
            print(f"{t.id:03d} | {status} | {t.titulo} (Prazo: {t.prazo})")

    def concluir_tarefa(self):
        self.listar_tarefas()
        try:
            tid = int(input("ID da tarefa a marcar como concluída: "))
            for t in self.tarefas:
                if t.id == tid:
                    t.concluir()
                    print("✔️ Tarefa marcada como concluída!")
                    return
            print("⚠️ Tarefa não encontrada.")
        except ValueError:
            print("⚠️ Entrada inválida.")

    def remover_tarefa(self):
        self.listar_tarefas()
        try:
            tid = int(input("ID da tarefa a remover: "))
            for t in self.tarefas:
                if t.id == tid:
                    self.tarefas.remove(t)
                    print("🗑️ Tarefa removida.")
                    return
            print("⚠️ Tarefa não encontrada.")
        except ValueError:
            print("⚠️ Entrada inválida.")

    def menu(self):
        while True:
            print("\n--- Gerenciador de Tarefas ---")
            print("1. Adicionar tarefa")
            print("2. Listar tarefas")
            print("3. Marcar tarefa como concluída")
            print("4. Remover tarefa")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.adicionar_tarefa()
            elif opcao == '2':
                self.listar_tarefas()
            elif opcao == '3':
                self.concluir_tarefa()
            elif opcao == '4':
                self.remover_tarefa()
            elif opcao == '5':
                self.salvar_tarefas()
                print("📁 Tarefas salvas. Saindo...")
