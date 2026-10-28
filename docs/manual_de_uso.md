# Manual de uso — TechBairro 3.3.2

## 1. Para que serve

A TechBairro é uma aplicação desktop para cadastrar, consultar, editar e excluir clientes fictícios de uma associação de moradores.

## 2. Requisitos

- Python 3 instalado.
- No Windows, use o instalador do Python que inclui o Tcl/Tk para disponibilizar o `tkinter`.
- Não são necessárias bibliotecas externas.

## 3. Iniciar o sistema

1. Baixe e extraia o pacote ZIP, ou clone o repositório.
2. Abra o terminal na pasta que contém `techbairro.py`.
3. Execute `python techbairro.py`.
4. Na primeira execução, a aplicação cria `techbairro.db` na mesma pasta do programa.

## 4. Cadastrar cliente

1. Preencha Nome, Telefone, E-mail e Endereço.
2. Use apenas números no telefone, sem espaços ou símbolos.
3. Informe um e-mail com usuário, `@` e ponto no domínio, como `ana@email.com`.
4. Clique em **Salvar**. A aplicação informa o resultado na tela.

Use somente dados fictícios em demonstrações e testes.

## 5. Consultar clientes

Clique em **Consultar Clientes** para abrir a lista de clientes cadastrados. A lista é exibida em ordem alfabética.

## 6. Editar cliente

1. Na consulta, selecione o cliente e clique em **Editar selecionado**; também é possível dar duplo clique no registro.
2. Altere os campos necessários.
3. Clique em **Salvar edição** para gravar as mudanças.
4. Clique em **Cancelar** para abandonar a edição.

## 7. Excluir cliente

1. Selecione o cliente na consulta.
2. Clique em **Excluir selecionado** ou pressione `Delete`.
3. Leia a mensagem de confirmação. Escolha **Não** para manter o cadastro ou **Sim** para confirmar a exclusão.

## 8. Dados e privacidade

Os registros são armazenados localmente em `techbairro.db`. Esse banco não deve ser publicado no GitHub. Para a avaliação, utilize exclusivamente dados fictícios.

## 9. Solução de problemas

- Se `python` não for reconhecido, confira se o Python está instalado e disponível no PATH; em alguns ambientes, o comando pode ser `py`.
- Se a janela não abrir, confirme que sua instalação do Python inclui `tkinter`.
- Se houver erro de banco, feche outras instâncias do programa e confira as permissões de gravação na pasta.
