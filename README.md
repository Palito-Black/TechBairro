# TechBairro 3.3.2

Sistema de **cadastro de clientes da associação de moradores**, com interface gráfica simples e banco de dados local SQLite.

## O que o sistema faz

- Cadastra clientes com nome, telefone, e-mail e endereço.
- Consulta clientes cadastrados em ordem alfabética.
- Edita um cadastro existente sem criar um duplicado.
- Exclui clientes após confirmação.
- Mostra a quantidade de clientes cadastrados.
- Valida campos obrigatórios, telefone numérico e formato básico do e-mail.

## Requisitos

- Python 3.10 ou superior recomendado.
- Windows 11 é o ambiente informado como testado no projeto. Outros sistemas não foram validados.
- O projeto usa apenas módulos da biblioteca padrão do Python: `tkinter` e `sqlite3`. Não há dependências externas para instalar.

## Instalação e execução

1. Baixe o ZIP da release ou clone o repositório.
2. Extraia os arquivos, se tiver baixado o ZIP.
3. Abra um terminal dentro da pasta do projeto.
4. Execute:

   ```bash
   python techbairro.py
   ```

Na primeira execução, o arquivo `techbairro.db` é criado automaticamente na pasta do programa. Esse arquivo contém os dados locais e não deve ser enviado ao GitHub.

## Como usar

1. Preencha os quatro campos e clique em **Salvar** para cadastrar.
2. Clique em **Consultar Clientes** para abrir a lista.
3. Selecione um cliente e use **Editar selecionado** ou **Excluir selecionado**. Também é possível dar duplo clique em um cliente para editar.
4. Confirme a exclusão quando solicitado.
5. Ao editar, confira os dados no formulário e clique em **Salvar edição**. Use **Cancelar** para abandonar a edição.

## Testes

Execute os testes automáticos de validação com:

```bash
python testar_validacao.py
```

Os seis casos manuais da entrega estão descritos em `docs/registro_de_testes.md`. Preencha a coluna “Obtido” após executar cada teste na interface.

## Estrutura do projeto

| Arquivo | Função |
|---|---|
| `techbairro.py` | Aplicação gráfica principal |
| `cliente.py` | Modelo de dados do cliente |
| `banco.py` | Operações de cadastro no SQLite |
| `validacao.py` | Regras de validação |
| `testar_validacao.py` | Testes automáticos das validações |
| `scripts/` | Scripts auxiliares de pacote e importação |
| `docs/manual_de_uso.md` | Manual de uso |
| `docs/registro_de_testes.md` | Registro dos testes da versão final |
| `docs/entrega_final.md` | Checklist e registro da entrega |
| `CHANGELOG.md` | Histórico de versões |

## Histórico e versão

Versão atual: **3.3.2**. O histórico detalhado está no `CHANGELOG.md`.

Para consultar o histórico de commits do repositório:

```bash
git log --oneline
```

## Repositório

https://github.com/Palito-Black/TechBairro

## Autor

Palito-Black
