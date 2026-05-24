# Registro e Autorizacao de App no Trello com Python para Agente de IA

## Sobre o Projeto

Este repositório foi criado como parte do desafio da DIO sobre registro e autorização de uma aplicação no Trello utilizando Python, com foco em preparar a integração para um agente de IA.

O objetivo é documentar o processo de criação de uma chave de API, geração de token de acesso e uso dessas credenciais em um script Python simples. Essa autorização é a base para que um agente de IA possa consultar quadros, listas e cartões no Trello de forma segura.

## Objetivos

- Entender como registrar uma aplicação no Trello;
- Gerar uma chave de API;
- Autorizar o acesso por token;
- Usar Python para consultar dados da API do Trello;
- Entender como essa autorização pode apoiar um agente de IA;
- Evitar exposição de credenciais no GitHub;
- Documentar o processo de forma clara e reutilizável.

## Tecnologias Utilizadas

- Python 3;
- API REST do Trello;
- Conceitos de agentes de IA;
- Git e GitHub;
- Variáveis de ambiente.

## Relacao com Agente de IA

Um agente de IA precisa acessar ferramentas externas para executar tarefas úteis. No contexto deste desafio, o Trello funciona como uma dessas ferramentas.

Com a autorização configurada, um agente poderia:

- Ler cartões de um quadro;
- Identificar tarefas atrasadas;
- Resumir atividades pendentes;
- Sugerir prioridades;
- Criar cartões a partir de comandos do usuário;
- Atualizar listas conforme o andamento das tarefas.

Antes de qualquer automação inteligente, é necessário garantir que o acesso ao Trello esteja funcionando corretamente e que as credenciais estejam protegidas.

Fluxo esperado:

```text
Usuário -> Agente de IA -> Script Python -> API do Trello -> Quadros e cartões
```

Neste repositório, o foco está na etapa inicial: registrar a aplicação, configurar credenciais e validar a autorização com Python.

## Etapas do Processo

### 1. Obter a chave da API

Para usar a API do Trello, é necessário acessar a área de desenvolvedor do Trello e gerar uma chave de API.

Essa chave identifica a aplicação que fará chamadas para a API.

### 2. Gerar o token de autorização

Depois de obter a chave, o usuário deve gerar um token autorizando a aplicação a acessar os recursos permitidos.

Esse token funciona como uma permissão de acesso e deve ser tratado como informação sensível.

### 3. Configurar variáveis de ambiente

As credenciais não devem ser escritas diretamente no código.

Exemplo:

```bash
TRELLO_API_KEY=sua_chave_aqui
TRELLO_TOKEN=seu_token_aqui
```

### 4. Executar o script Python

O arquivo [`src/trello_auth_check.py`](src/trello_auth_check.py) faz uma chamada simples para validar se a autenticação está funcionando.

```bash
python src/trello_auth_check.py
```

Se as credenciais estiverem corretas, o programa exibe informações básicas do usuário autenticado.

## Estrutura do Repositório

```text
.
├── README.md
├── .env.example
├── .gitignore
└── src/
    └── trello_auth_check.py
```

## Cuidados de Segurança

- Nunca publique sua chave de API real no GitHub;
- Nunca publique seu token real no GitHub;
- Use variáveis de ambiente;
- Revogue tokens antigos caso eles sejam expostos;
- Mantenha o arquivo `.env` fora do versionamento;
- Use `.env.example` apenas como modelo.

## Exemplo de Uso

Com as variáveis configuradas, execute:

```bash
python src/trello_auth_check.py
```

Saída esperada:

```text
Autenticacao realizada com sucesso.
Usuario: nome_do_usuario
Nome completo: Nome Completo
```

## Aprendizados

Este desafio reforçou a importância de separar código e credenciais. Em integrações com APIs externas, não basta fazer a requisição funcionar; também é necessário proteger tokens, organizar a documentação e garantir que outras pessoas consigam reproduzir o processo com segurança.

Também ficou claro que um agente de IA depende de integrações bem configuradas. Sem autenticação segura, o agente não consegue acessar dados externos nem executar ações em ferramentas como o Trello.

## Referências

- Documentação da API do Trello
- Trello Developer API Keys
- Python Documentation
