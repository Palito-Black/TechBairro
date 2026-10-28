# Registro de testes da TechBairro

Versão testada: 3.3.2  · Data: **preencher após executar** · Responsável: **preencher**

Sistema operacional e versão do Python: **preencher com o ambiente usado no teste**

> Instrução: execute cada caso na interface da versão final. Preencha “Obtido” com a mensagem exatamente como aparece na tela. Não marque como aprovado antes de executar.

| ID | Requisito | Passos e dados | Esperado | Obtido (preencher após executar) | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente fictício com todos os campos corretos | A tela deve exibir exatamente: `Cliente cadastrado com sucesso!`; o cliente deve aparecer na consulta | Pendente de execução manual | Pendente |
| CT02 | RF01 | Deixar Nome e Endereço vazios e tentar salvar | A tela deve exibir exatamente: `Erro: todos os campos precisam estar preenchidos!` | Pendente de execução manual | Pendente |
| CT03 | RF02 | Informar o telefone `61 9999 0000` com espaços | A tela deve exibir exatamente: `Erro: o telefone deve conter apenas números!` | Pendente de execução manual | Pendente |
| CT04 | RF03 | Informar o e-mail `ana@email` | A tela deve exibir exatamente: `Erro: digite um e-mail válido!` | Pendente de execução manual | Pendente |
| CT05 | RF05 | Editar um cliente existente, trocar o telefone por um valor válido e salvar | A tela deve exibir `Cliente 'Ana Souza' atualizado com sucesso!` (se esse for o nome fictício usado); o telefone deve mudar na consulta e o total de cadastros não deve aumentar | Pendente de execução manual | Pendente |
| CT06 | RF06 | Tentar excluir um cliente; responder Não e depois repetir respondendo Sim | Ao responder `Não`, a janela de confirmação fecha e o cliente permanece. Ao responder `Sim`, a tela deve exibir exatamente: `Cliente excluído com sucesso.` e o cliente deixa de aparecer na consulta | Pendente de execução manual | Pendente |

## Testes automáticos

Comando: `python testar_validacao.py`

Resultado da execução feita após as alterações: **Todos os testes passaram.** Saída observada: `OK teste_cliente_valido`, `OK teste_endereco_vazio`, `OK teste_telefone_com_letras`, `OK teste_email_sem_ponto`, `OK teste_nome_e_telefone_vazios`, `OK teste_email_sem_usuario`, `Todos os testes passaram.`

## Defeitos encontrados

Preencher após executar os testes manuais. Descrever o defeito, como foi corrigido e o commit correspondente, ou escrever “nenhum” se nenhum defeito for encontrado.
