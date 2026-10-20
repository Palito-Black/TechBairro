import sqlite3
from cliente import Cliente


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


