# TechBairro 3.3.1

Sistema de **cadastro de clientes da associação de moradores**, com interface gráfica simples e banco de dados local.

## O que ele faz

- Cadastra clientes com **nome, telefone, e-mail e endereço**
- Consulta todos os clientes cadastrados (em ordem alfabética)
- Edita um cliente já cadastrado (botão ou duplo clique na lista)
- Exclui um cliente, com mensagem de confirmação (botão ou tecla `Delete`)
- Mostra o total de clientes cadastrados na tela principal
- Valida os dados antes de salvar:
  - todos os campos são obrigatórios
  - o telefone deve conter apenas números
  - o e-mail precisa ter um formato válido (`usuario@dominio.com`)

## Requisitos

- Python 3
- Windows 11 (é o único sistema testado; não há suporte a outros sistemas operacionais)

Não é preciso instalar nada além do Python. O projeto usa apenas bibliotecas que já vêm com ele: `tkinter` (interface) e `sqlite3` (banco de dados).

## Como executar

1. Baixe ou clone o repositório:
   ```
   git clone https://github.com/Palito-Black/TechBairro.git
   cd TechBairro
   ```
2. Execute o programa:
   ```
   python techbairro_v3.3.1.py
   ```

Na primeira execução o arquivo `techbairro.db` é criado automaticamente na pasta do projeto.

## Como usar

1. Preencha os campos e clique em **Salvar** para cadastrar um cliente.
2. Clique em **Consultar Clientes** para ver a lista.
3. Na lista, selecione um cliente e use **Editar selecionado** ou **Excluir selecionado**.
4. Ao editar, os dados voltam para o formulário e o botão muda para **Salvar edição**. Use **Cancelar** para desistir da edição ou limpar o formulário.

## Estrutura do projeto

| Arquivo | Função |
|---|---|
| `techbairro_v3.3.1.py` | Programa principal e interface gráfica |
| `cliente.py` | Classe `Cliente` (dados do cliente) |
| `banco.py` | Classe `GerenciadorClientes` (acesso ao banco SQLite) |
| `validacao.py` | Classe `ValidadorCliente` (regras de validação) |
| `testar_validacao.py` | Testes das regras de validação |
| `scripts/` | Scripts auxiliares |
| `CHANGELOG.md` | Histórico de mudanças por versão |
| `COMO_EXECUTAR.txt` | Instruções rápidas de execução |

## Histórico de versões

As mudanças de cada versão estão no [CHANGELOG](CHANGELOG.md). Para ver o histórico do código com Git:

```
git log --oneline
```

## Autor

[Palito-Black](https://github.com/Palito-Black)
