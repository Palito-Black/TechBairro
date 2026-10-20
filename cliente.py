# =========================================================
# CLIENTE (Aula 21)
# =========================================================
# Responsabilidade: representar os dados de um cliente.
# Este arquivo não sabe nada de janela nem de banco.


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
