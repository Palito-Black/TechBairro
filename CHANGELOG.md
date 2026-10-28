# Changelog TechBairro

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## Em desenvolimento
### Adicionado
- Código publicado no GitHub, com histórico de verções

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## v3.3.2 (Aula 27)

### Adicionado
- README atualizado com requisitos, instalação, execução e estrutura do projeto.
- Manual de uso em `docs/manual_de_uso.md`.
- Registro de testes em `docs/registro_de_testes.md`.
- Registro de entrega em `docs/entrega_final.md`.
- Arquivo `requirements.txt` para documentar as dependências do projeto.

### Alterado
- Nome do programa principal padronizado para `techbairro.py`.
- Aplicação utiliza as classes `Cliente` e `GerenciadorClientes` dos módulos separados.
- Gerador de pacote atualizado para a versão 3.3.2 e ajustado para não incluir o próprio ZIP no pacote.

## v3.3.1

### Alterado
- A classe Cliente foi separada para o arquivo cliente.py.
- A classe GerenciadorClientes foi separada para o arquivo banco.py.
- As regras de validação foram centralizadas na classe ValidadorCliente, em validacao.py.
- O techbairro.py importa as classes dos módulos separados.

### Testes
- Adicionado o arquivo testar_validacao.py para testar as regras sem abrir a janela.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## v3.3.0

### Adicionado

- Modo de edição identificado pelo ID do cliente, evitando criar um cadastro duplicado ao editar.
- Atalho Delete para excluir o cliente selecionado na consulta.
- Duplo clique em um cliente para abrir a edição.
- Confirmação antes de excluir um cadastro.
### Alterado

- O formulário mostra quando um cliente está sendo editado.
- O banco é aberto pelo caminho completo (os.path + __file__), sempre na pasta do projeto.
- A mensagem "Banco em uso" mostra no terminal o caminho do arquivo SQLite utilizado.
### Corrigido

- A lista da consulta é atualizada depois de excluir um cliente.
- A edição atualiza o cadastro existente pelo ID, sem adicionar outro registro.
- O atalho Delete só exclui o cliente selecionado e pede confirmação.
- A abertura de mais de uma janela de consulta é tratada para evitar atalhos ligados à janela errada.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## v3.2.1

### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

### Alterado
- O banco agora é aberto pelo caminho completo (`os.path` + `__file__`), sempre na pasta do projeto, não importa de onde o programa seja executado.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## v3.1

### Corrigido
- O método `atualizar()` agora faz `commit`, e as alterações passam a ser salvas no banco.
- A validação de e-mail agora recusa endereços sem ponto depois do `@`.
- A mensagem de erro do e-mail agora informa "formato inválido".

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

## v3.0

### Adicionado
- Interface gráfica principal (cadastro), com formulário e botões de salvar, cancelar e consultar clientes.

### Alterado
- O `GerenciadorClientes` deixou de guardar os clientes em uma lista na memória e passou a gravá-los no banco SQLite `techbairro.db`.
- A tela passou a usar os ids do banco em vez dos índices da lista.
- As operações de CRUD (adicionar, listar, atualizar e remover) agora persistem no banco.