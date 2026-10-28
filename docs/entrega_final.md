# Entrega final da TechBairro

Aluno(a): **preencher** · Versão entregue: **3.3.2 (confirmar após testes)**

Por que esse número de versão: a mudança prevista nesta entrega é principalmente documentação e ajustes de empacotamento; por isso, incrementa-se o último número da versão 3.3.1 para 3.3.2. Se houver alteração funcional adicional, confirmar a regra com o professor.

| # | Item | Evidência | Status
|---|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | `docs/registro_de_testes.md` — preencher após executar | Pendente |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | Captura da janela + `CHANGELOG.md` + `README.md` | Pendente |
| 3 | O pacote foi testado numa pasta limpa | Registrar caminho e resultado do teste do ZIP extraído | Pendente |
| 4 | Tag e release publicadas, com o ZIP anexado | Link da release: **preencher** | Pendente |
| 5 | O repositório não tem banco, `__pycache__` nem `dist` | Conferir arquivos rastreados no GitHub | Pendente |
| 6 | O histórico tem commits com mensagens claras | Link dos commits: **preencher** | Pendente |
| 7 | README, manual de uso e requirements.txt estão no repositório | `README.md`, `docs/manual_de_uso.md`, `requirements.txt` | Pendente |
| 8 | A Issue “Teste do README” (Aula 26) está fechada | Link ou captura da Issue: **preencher** | Pendente |
| 9 | O vídeo está publicado e o link abre sem pedir login | Link do vídeo: **preencher** | Pendente |

## Roteiro do vídeo (até 3 minutos)

| Bloco | Tempo | O que mostrar ou dizer |
|---|---:|---|
| 1. Problema e solução | 30 s | Apresentar a TechBairro 3.3.2 como sistema desktop para cadastro e gerenciamento de clientes fictícios da associação. |
| 2. Demonstração | 1 min 30 s | Mostrar cadastro, consulta, edição, exclusão com confirmação e uma validação rejeitando dado inválido. |
| 3. Como foi construída | 30 s | Explicar interface Tkinter, banco SQLite, módulos separados, testes automáticos e repositório/release no GitHub. |
| 4. Aprendizado | 30 s | Relatar uma dificuldade real encontrada e como foi resolvida, ou uma melhoria que faria. |

## Perguntas

**1. Por que o arquivo `techbairro.db` não está no GitHub?**

Porque ele armazena os dados locais dos clientes e é gerado automaticamente na execução. Não deve ser compartilhado no repositório; para testes e demonstrações devem ser usados dados fictícios.

**2. Qual caso de teste pegou um defeito de verdade? Qual era o defeito?**

Preencher com base nos testes realmente executados. Se nenhum defeito for encontrado nesta entrega, mencionar um caso de teste anterior das Aulas 15, 20 ou 21 que tenha revelado um defeito real, conforme solicitado pelo professor.

**3. Se o voluntário tiver só o link do repositório, como instala e executa a TechBairro?**

Pode clonar o repositório ou baixar o ZIP, instalar Python 3 com suporte ao Tkinter, abrir o terminal na pasta do projeto e executar `python techbairro.py`. A aplicação cria o banco local automaticamente na primeira execução.

## Autoavaliação (até 5 linhas)

Preencher depois de gravar e assistir ao vídeo: mencionar o que ficou bom, o que mudaria e o principal aprendizado da unidade curricular.
