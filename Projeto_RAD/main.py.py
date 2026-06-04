import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def atualizar_lista():
    lista_tarefas.delete(0, tk.END)

    for tarefa in tarefas:
        status = "✅" if tarefa["concluida"] else "⬜"
        lista_tarefas.insert(
            tk.END,
            f"{status} {tarefa['nome']}"
        )

    label_total.config(
        text=f"Total de tarefas: {len(tarefas)}"
    )


def adicionar_tarefa():
    nome = entrada_tarefa.get().strip()

    if nome == "":
        messagebox.showwarning(
            "Aviso",
            "Digite uma tarefa."
        )
        return

    tarefas.append({
        "nome": nome,
        "concluida": False
    })

    salvar_tarefas()
    atualizar_lista()
    entrada_tarefa.delete(0, tk.END)


def editar_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]

        novo_nome = simpledialog.askstring(
            "Editar Tarefa",
            "Digite o novo nome:"
        )

        if novo_nome and novo_nome.strip():
            tarefas[indice]["nome"] = novo_nome

            salvar_tarefas()
            atualizar_lista()

    except:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma tarefa."
        )


def excluir_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]

        resposta = messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta tarefa?"
        )

        if resposta:
            tarefas.pop(indice)

            salvar_tarefas()
            atualizar_lista()

    except:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma tarefa."
        )


def concluir_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]

        tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]

        salvar_tarefas()
        atualizar_lista()

    except:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma tarefa."
        )


# JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("900x700")
janela.configure(bg="#f5f7fa")
janela.resizable(True,True)

tarefas = carregar_tarefas()

# TÍTULO
titulo = tk.Label(
    janela,
    text="📋 Gerenciador de Tarefas",
    font=("Segoe UI", 20, "bold"),
    bg="#f5f7fa",
    fg="#2c3e50"
)
titulo.pack(pady=20)

# CAMPO DE TEXTO
entrada_tarefa = tk.Entry(
    janela,
    width=40,
    font=("Segoe UI", 12)
)
entrada_tarefa.pack(pady=10)

# BOTÃO ADICIONAR
botao_adicionar = tk.Button(
    janela,
    text="➕ Adicionar Tarefa",
    font=("Segoe UI", 10, "bold"),
    bg="#27ae60",
    fg="white",
    width=20,
    command=adicionar_tarefa
)
botao_adicionar.pack(pady=10)

# CONTADOR
label_total = tk.Label(
    janela,
    text="Total de tarefas: 0",
    font=("Segoe UI", 10),
    bg="#f5f7fa",
    fg="#555555"
)
label_total.pack()

# LISTA
lista_tarefas = tk.Listbox(
    janela,
    width=60,
    height=12,
    font=("Segoe UI", 11),
    bd=2
)
lista_tarefas.pack(pady=15)

# FRAME DOS BOTÕES
frame_botoes = tk.Frame(
    janela,
    bg="#f5f7fa"
)
frame_botoes.pack()

# BOTÃO EDITAR
btn_editar = tk.Button(
    frame_botoes,
    text="✏️ Editar",
    bg="#3498db",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold"),
    command=editar_tarefa
)
btn_editar.grid(
    row=0,
    column=0,
    padx=5
)

# BOTÃO EXCLUIR
btn_excluir = tk.Button(
    frame_botoes,
    text="🗑 Excluir",
    bg="#e74c3c",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold"),
    command=excluir_tarefa
)
btn_excluir.grid(
    row=0,
    column=1,
    padx=5
)

# BOTÃO CONCLUIR
btn_concluir = tk.Button(
    frame_botoes,
    text="✅ Concluir",
    bg="#f39c12",
    fg="white",
    width=15,
    font=("Segoe UI", 10, "bold"),
    command=concluir_tarefa
)
btn_concluir.grid(
    row=0,
    column=2,
    padx=5
)

atualizar_lista()

janela.mainloop()