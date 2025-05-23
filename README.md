# Kanban Board em Docker

Uma aplicação simples de Kanban Board para gerenciamento de tarefas, executando em Docker.

## Funcionalidades

- Visualização de quadro Kanban com colunas "A Fazer", "Em Andamento" e "Concluído"
- Adicionar novos cartões em qualquer coluna
- Mover cartões entre colunas
- Excluir cartões
- Persistência de dados em arquivo JSON

## Como executar

### Pré-requisitos

- Docker
- Docker Compose

### Passos para executar

1. Clone ou baixe este repositório
2. Navegue até a pasta do projeto
3. Execute o comando:

```bash
docker-compose up --build
```

4. Acesse a aplicação em seu navegador:

```
http://localhost:5000
```

## Como testar

1. Adicione um novo cartão em qualquer coluna preenchendo o título e descrição
2. Mova cartões entre as colunas usando o botão "Mover"
3. Exclua cartões usando o botão "Excluir"
4. Verifique se os dados persistem mesmo após reiniciar o contêiner

## Estrutura do projeto

```
kanban/
├── app/
│   ├── app.py              # Aplicação Flask
│   ├── kanban_data.json    # Arquivo de dados (criado automaticamente)
│   ├── requirements.txt    # Dependências Python
│   └── templates/
│       └── index.html      # Template da interface
├── Dockerfile              # Configuração da imagem Docker
└── docker-compose.yml      # Configuração do Docker Compose
```

# Criar um novo repositório no GitHub pelo navegador e depois executar:
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
git push -u origin main
