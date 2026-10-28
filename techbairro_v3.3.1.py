import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente


# Versão
VERSAO = "3.3.1"


# Classe do cliente
class Cliente:
    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return (
            self.nome + " | " +
            self.telefone + " | " +
            self.email + " | " +
            self.endereco
        )

    def iniciais(self):
        partes = self.nome.split()

        if len(partes) >= 2:
            return partes[0][0].upper() + partes[-1][0].upper()

        return self.nome[:2].upper()


# Classe que mexe no banco de dados
class GerenciadorClientes:
    def __init__(self, caminho_banco="techbairro.db"):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    # Criar a tabela
    def criar_tabela(self):
        conexao = self.conectar()
        try:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    email TEXT,
                    endereco TEXT
                )
            """)
            conexao.commit()
        finally:
            conexao.close()

    # Cadastrar
    def adicionar(self, cliente):
        conexao = self.conectar()
        try:
            cursor = conexao.execute(
                "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
                (
                    cliente.nome,
                    cliente.telefone,
                    cliente.email,
                    cliente.endereco
                )
            )
            cliente.id = cursor.lastrowid
            conexao.commit()
        finally:
            conexao.close()

    # Listar
    def listar(self):
        conexao = self.conectar()
        try:
            registros = conexao.execute(
                "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"
            ).fetchall()
        finally:
            conexao.close()

        clientes = []
        for linha in registros:
            cliente = Cliente(
                linha[1],
                linha[2] or "",
                linha[3] or "",
                linha[4] or "",
                linha[0]
            )
            clientes.append(cliente)

        return clientes

    # Atualizar
    def atualizar(self, id_cliente, novo_cliente):
        conexao = self.conectar()
        try:
            cursor = conexao.execute(
                """
                UPDATE clientes
                SET nome = ?, telefone = ?, email = ?, endereco = ?
                WHERE id = ?
                """,
                (
                    novo_cliente.nome,
                    novo_cliente.telefone,
                    novo_cliente.email,
                    novo_cliente.endereco,
                    id_cliente
                )
            )
            conexao.commit()
            alterado = cursor.rowcount
        finally:
            conexao.close()

        # Retorna True se uma linha foi alterada
        return alterado > 0

    # Excluir
    def remover(self, id_cliente):
        conexao = self.conectar()
        try:
            cursor = conexao.execute(
                "DELETE FROM clientes WHERE id = ?",
                (id_cliente,)
            )
            conexao.commit()
            removido = cursor.rowcount
        finally:
            conexao.close()

        # Retorna True se uma linha foi removida
        return removido > 0

    # Total
    def total(self):
        conexao = self.conectar()
        try:
            quantidade = conexao.execute(
                "SELECT COUNT(*) FROM clientes"
            ).fetchone()[0]
        finally:
            conexao.close()

        return quantidade


# Banco de dados
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print("Banco em uso: " + CAMINHO_BANCO)


# Janela principal
root = tk.Tk()
root.title("TechBairro — Cadastro de Cliente")
root.geometry("500x420")
root.resizable(False, False)
root.config(bg="#2c3e50")

try:
    gerenciarclientes = GerenciadorClientes(CAMINHO_BANCO)
    validador = ValidadorCliente()
except sqlite3.Error as erro:
    messagebox.showerror("Erro", "Erro ao abrir o banco de dados:\n" + str(erro))
    root.destroy()
    raise

id_em_edicao = None
consultas_abertas = []


# Limpar campos
def limparcampos(sair_da_edicao=True):
    global id_em_edicao

    entrynome.delete(0, tk.END)
    entrytelefone.delete(0, tk.END)
    entryemail.delete(0, tk.END)
    entryendereco.delete(0, tk.END)

    if sair_da_edicao:
        id_em_edicao = None
        botao_salvar.config(text="Salvar")


# Validação de e-mail
def email_parece_valido(email):
    if "@" not in email:
        return False

    usuario, _, dominio = email.partition("@")

    if usuario == "" or "." not in dominio:
        return False

    return True


# Atualizar consultas abertas
def atualizar_consultas_abertas():
    consultas_validas = []

    for consulta, atualizar_lista in consultas_abertas:
        if consulta.winfo_exists():
            atualizar_lista()
            consultas_validas.append((consulta, atualizar_lista))

    consultas_abertas[:] = consultas_validas


# Salvar
def salvarcliente():
    global id_em_edicao

    nome = entrynome.get().strip()
    telefone = entrytelefone.get().strip()
    email = entryemail.get().strip()
    endereco = entryendereco.get().strip()

    # Cria o cliente para validar os dados
    cliente = Cliente(
        nome,
        telefone,
        email,
        endereco,
        id_em_edicao
    )

    # MUDOU NA AULA 21: as regras ficam no ValidadorCliente
    erro = validador.validar(cliente)
    if erro is not None:
        # Mantém as mensagens que a tela já mostrava na versão 3.3.0
        if erro.startswith("Preencha o(s) campo(s):"):
            mensagem = "Erro: todos os campos precisam estar preenchidos!"
        elif erro == "Telefone inválido: use somente números.":
            mensagem = "Erro: o telefone deve conter apenas números!"
        else:
            mensagem = "Erro: digite um e-mail válido!"

        labelstatus.config(
            text=mensagem,
            fg="red"
        )
        return

    try:
        if id_em_edicao is None:
            gerenciarclientes.adicionar(cliente)
            labelstatus.config(
                text="Cliente cadastrado com sucesso!",
                fg="green"
            )

        else:
            # MUDOU NA AULA 20: confere se o banco alterou alguma linha
            alterou = gerenciarclientes.atualizar(
                id_em_edicao,
                cliente
            )

            # NOVO NA AULA 20: trata o cliente removido durante a edição
            if not alterou:
                labelstatus.config(
                    text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                    fg="red"
                )
                limparcampos()
                return

            labelstatus.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except sqlite3.Error as erro:
        labelstatus.config(
            text="Erro no banco de dados: " + str(erro),
            fg="red"
        )
        return

    labelcontador.config(
        text="Clientes cadastrados: " + str(gerenciarclientes.total())
    )

    limparcampos()
    atualizar_consultas_abertas()


# Cancelar
def cancelar():
    estava_editando = id_em_edicao is not None

    limparcampos()

    if estava_editando:
        labelstatus.config(
            text="Edição cancelada. Nada foi alterado.",
            fg="gray"
        )
    else:
        labelstatus.config(
            text="Formulário limpo",
            fg="gray"
        )


# Janela de consulta
def abrirconsulta():
    consulta = tk.Toplevel(root)
    consulta.title("Consulta de Clientes")
    consulta.geometry("1000x350")
    consulta.resizable(False, False)
    consulta.config(bg="#2c3e50")

    lista_consulta = tk.Listbox(
        consulta,
        width=100,
        height=12
    )

    lista_consulta.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    scrollbar = tk.Scrollbar(consulta)
    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )

    lista_consulta.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista_consulta.yview)

    framebotoes = tk.Frame(
        consulta,
        bg="#2c3e50"
    )
    framebotoes.pack(
        side="bottom",
        pady=10
    )

    # NOVO NA AULA 20: guarda os clientes na ordem exibida
    clientes_na_tela = []

    # Atualizar lista
    def atualizar_lista_consulta():
        lista_consulta.delete(0, tk.END)

        # NOVO NA AULA 20: limpa a lista que corresponde à tela
        clientes_na_tela.clear()

        try:
            clientes_cadastrados = gerenciarclientes.listar()
        except sqlite3.Error as erro:
            lista_consulta.insert(tk.END, f"Erro ao ler o banco: {erro}")
            return

        if not clientes_cadastrados:
            lista_consulta.insert(tk.END, "Nenhum cliente cadastrado")
            return

        for cliente in clientes_cadastrados:
            lista_consulta.insert(tk.END, cliente.resumo())
            # NOVO NA AULA 20: mantém cliente e linha na mesma posição
            clientes_na_tela.append(cliente)

    atualizar_lista_consulta()

    # Cliente selecionado
    def cliente_selecionado(acao):
        selecionado = lista_consulta.curselection()

        # NOVO NA AULA 20: também recusa linhas de aviso
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning(
                "Atenção",
                f"Selecione um cliente antes de {acao}."
            )
            return None

        return clientes_na_tela[selecionado[0]]

    # Editar cliente
    def editarcliente():
        global id_em_edicao

        # MUDOU NA AULA 20: usa o cliente que aparece na linha selecionada
        cliente = cliente_selecionado("editar")
        if cliente is None:
            return

        id_em_edicao = cliente.id
        limparcampos(sair_da_edicao=False)

        entrynome.insert(0, cliente.nome)
        entrytelefone.insert(0, cliente.telefone)
        entryemail.insert(0, cliente.email)
        entryendereco.insert(0, cliente.endereco)

        labelstatus.config(
            text="Editando cliente: " + cliente.nome,
            fg="#CBD5E1"
        )

        # NOVO NA AULA 20: deixa o modo de edição visível
        botao_salvar.config(text="Salvar edição")
        consulta.destroy()

    # Excluir cliente
    def excluircliente():
        # MUDOU NA AULA 20: usa o cliente que aparece na linha selecionada
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return

        # NOVO NO DESAFIO: exibe outros dados para confirmar a pessoa
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja realmente excluir o cliente:\n\n" +
            cliente.nome + "\n" +
            "Telefone: " + cliente.telefone + "\n" +
            "E-mail: " + cliente.email + "?"
        )

        if not confirmar:
            return

        try:
            # MUDOU NA AULA 20: guarda a resposta do banco
            removeu = gerenciarclientes.remover(cliente.id)
        except sqlite3.Error as erro:
            messagebox.showerror(
                "Erro",
                "Não foi possível excluir o cliente.\n" + str(erro)
            )
            return

        # NOVO NA AULA 20: trata o cliente removido em outra janela
        if not removeu:
            messagebox.showwarning(
                "Cliente não encontrado",
                f"{cliente.nome} já não está mais no banco.\n"+
                "A lista será atualizada."
            )
            atualizar_lista_consulta()
            labelcontador.config(
                text="Clientes cadastrados: " + str(gerenciarclientes.total())
            )
            return

        atualizar_lista_consulta()

        labelcontador.config(
            text="Clientes cadastrados: " + str(gerenciarclientes.total())
        )

        labelstatus.config(
            text="Cliente excluído com sucesso.",
            fg="green"
        )

    # Botões da consulta
    buttoneditar = tk.Button(
        framebotoes,
        font=("Times", 10),
        text="Editar selecionado",
        width=18,
        command=editarcliente,
        bg="#2c3e50",
        fg="#CBD5E1"
    )
    buttoneditar.grid(
        row=0,
        column=0,
        padx=10
    )

    buttonexcluir = tk.Button(
        framebotoes,
        font=("Times", 10),
        text="Excluir selecionado",
        width=18,
        command=excluircliente,
        bg="#2c3e50",
        fg="#CBD5E1"
    )
    buttonexcluir.grid(
        row=0,
        column=1,
        padx=10
    )

    # NOVO NA AULA 20: duplo clique abre a edição
    lista_consulta.bind(
        "<Double-Button-1>",
        lambda evento: editarcliente()
    )

    # NOVO NO DESAFIO: Delete usa a mesma confirmação do botão
    lista_consulta.bind(
        "<Delete>",
        lambda evento: excluircliente()
    )

    # Mantém cada janela de consulta com sua própria lista
    consultas_abertas.append((consulta, atualizar_lista_consulta))

    def fechar_consulta():
        consulta.destroy()

    consulta.protocol("WM_DELETE_WINDOW", fechar_consulta)


# Título
frametitle = tk.Frame(
    root,
    bg="#2c3e50"
)
frametitle.pack(fill="x")

labeltitle = tk.Label(
    frametitle,
    font=("Times", 18, "bold"),
    text="Cadastro de Cliente",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labeltitle.pack(pady=20)


# Formulário
frame1 = tk.Frame(
    root,
    bg="#2c3e50"
)
frame1.pack(pady=5)

labelnome = tk.Label(
    frame1,
    font=("Times", 11),
    text="Nome:",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labelnome.grid(row=0, column=0, padx=10, pady=8, sticky="e")

entrynome = tk.Entry(frame1, width=30)
entrynome.grid(row=0, column=1, padx=10, pady=8)

labeltelefone = tk.Label(
    frame1,
    font=("Times", 11),
    text="Telefone:",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labeltelefone.grid(row=1, column=0, padx=10, pady=8, sticky="e")

entrytelefone = tk.Entry(frame1, width=30)
entrytelefone.grid(row=1, column=1, padx=10, pady=8)

labelemail = tk.Label(
    frame1,
    font=("Times", 11),
    text="E-mail:",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labelemail.grid(row=2, column=0, padx=10, pady=8, sticky="e")

entryemail = tk.Entry(frame1, width=30)
entryemail.grid(row=2, column=1, padx=10, pady=8)

labelendereco = tk.Label(
    frame1,
    font=("Times", 11),
    text="Endereço:",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labelendereco.grid(row=3, column=0, padx=10, pady=8, sticky="e")

entryendereco = tk.Entry(frame1, width=30)
entryendereco.grid(row=3, column=1, padx=10, pady=8)


# Status
labelstatus = tk.Label(
    root,
    font=("Times", 10, "bold"),
    text="Preencha os dados do cliente.",
    bg="#2c3e50",
    fg="#CBD5E1"
)
labelstatus.pack(pady=8)

labelcontador = tk.Label(
    root,
    font=("Times", 10),
    text="Clientes cadastrados: " + str(gerenciarclientes.total()),
    bg="#2c3e50",
    fg="#CBD5E1"
)
labelcontador.pack(pady=3)


# Botões principais
frame2 = tk.Frame(
    root,
    bg="#2c3e50"
)
frame2.pack(pady=5)

# MUDOU NA AULA 20: guarda o botão para alterar seu texto
botao_salvar = tk.Button(
    frame2,
    font=("Times", 10),
    text="Salvar",
    width=10,
    command=salvarcliente,
    bg="#2c3e50",
    fg="#CBD5E1"
)
botao_salvar.grid(
    row=4,
    column=0,
    padx=5,
    pady=5
)

button1 = tk.Button(
    frame2,
    font=("Times", 10),
    text="Cancelar",
    width=10,
    command=cancelar,
    bg="#2c3e50",
    fg="#CBD5E1"
)
button1.grid(
    row=4,
    column=1,
    padx=5,
    pady=5
)

button2 = tk.Button(
    frame2,
    font=("Times", 10),
    text="Consultar Clientes",
    width=18,
    command=abrirconsulta,
    bg="#2c3e50",
    fg="#CBD5E1"
)
button2.grid(
    row=5,
    column=0,
    columnspan=2,
    padx=10,
    pady=5
)


# Versão
labelversao = tk.Label(
    root,
    font=("Times", 8),
    text=f"v{VERSAO}",
    fg="#CBD5E1",
    bg="#2c3e50"
)
labelversao.place(
    relx=0.96,
    rely=0.95,
    anchor="se"
)


root.mainloop()