# Projeto: Sistema de Biblioteca com Polyglot Persistence

## Visão Geral

Este projeto tem como objetivo aplicar o conceito de **Polyglot Persistence**, utilizando múltiplos bancos de dados de acordo com o tipo de dado e sua finalidade dentro da aplicação.

O sistema desenvolvido é uma **biblioteca**, com funcionalidades de:

* Cadastro de usuários
* Cadastro de livros
* Controle de empréstimos
* Consulta de dados

A arquitetura segue o modelo:

```
Frontend <--> Backend <--> PostgreSQL
                         <--> Redis
                         <--> MongoDB
```

---

## Tecnologias Utilizadas

### Backend

* Python
* FastAPI
* SQLAlchemy

### Bancos de Dados

* PostgreSQL (Relacional)
* Redis (NoSQL - chave/valor)
* MongoDB (NoSQL - documentos)

### Infraestrutura

* Docker / Docker Compose (execução local)
* MongoDB Atlas (web)

---

## Modelagem Relacional

A modelagem relacional foi construída de forma **simples e direta**, respeitando as regras de negócio do sistema.

### Regra importante

* Cada **livro possui apenas um autor**
* Cada **empréstimo está associado a apenas um livro**
* Portanto, **não existem relacionamentos N:N neste modelo**

---

### Entidades

* User (Usuário)
* Book (Livro)
* Author (Autor)
* Loan (Empréstimo)

---

### Diagrama do Modelo Relacional

![Modelo Relacional](./docs/mer_biblioteca.png)

---

### Relacionamentos

* Um **usuário** pode ter vários empréstimos (1:N)
* Um **livro** pode aparecer em vários empréstimos (1:N)
* Um **autor** pode ter vários livros (1:N)

---

## Uso dos Bancos de Dados

### PostgreSQL (RDB)

Responsável pelos dados **transacionais e estruturados**:

* Usuários
* Livros
* Autores
* Empréstimos

  Justificativa:

* Garantia de consistência (ACID)
* Estrutura relacional bem definida
* Ideal para operações CRUD

---

### Redis (NoSQL - Key/Value)

Utilizado como camada de **cache e desempenho**.

#### O que será armazenado:

* Livros mais acessados
* Empréstimos recentes
* Cache de consultas (ex: busca de livros)

#### Estrutura de chaves (exemplos):

```
book:{id} -> dados do livro
user:{id}:loans -> lista de empréstimos
top_books -> ranking de livros populares
```

#### Estratégias:

* TTL (tempo de expiração) para cache
* Redução de carga no PostgreSQL
* Respostas mais rápidas para o frontend

💡 Justificativa:

* Alta performance (in-memory)
* Ideal para leitura rápida
* Reduz latência da aplicação

---

### 🍃 MongoDB (NoSQL - Document)

Responsável por dados **semi-estruturados e históricos**.

#### 📌 O que será armazenado:

* Histórico completo de empréstimos
* Logs de atividades
* Possíveis avaliações de livros

#### 📌 Exemplo de documento:

```json
{
  "id_user": 1,
  "book_id": 10,
  "loan_date": "2026-04-10",
  "return_date": "2026-04-15",
  "status": "returned"
}
```

💡 Justificativa:

* Flexibilidade de schema
* Ideal para logs e histórico
* Escalabilidade horizontal

---

## Backend (FastAPI)

O backend será responsável por:

* Expor endpoints REST (CRUD completo)
* Integrar com os três bancos
* Gerenciar regras de negócio

### Estrutura esperada:

```
app/
 ├── routes/
 ├── services/
 ├── models/
 ├── schemas/
 ├── database/
```

---

### 📡 Exemplos de endpoints

#### Usuários

* `POST /users`
* `GET /users`
* `GET /users/{id}`

#### Livros

* `POST /books`
* `GET /books`

#### Empréstimos

* `POST /loans`
* `GET /loans`

---

## ▶️ Como executar o projeto

### 1. Clonar repositório

```bash
git clone <repo_url>
cd projeto-biblioteca
```

### 2. Subir containers

```bash
docker-compose up -d
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar aplicação

```bash
uvicorn app.main:app --reload
```

---

## Requisitos para execução

* Docker instalado
* Python 3.10+
* Acesso ao MongoDB Atlas configurado

---

## Objetivo do Projeto

Demonstrar na prática:

* Uso de múltiplos bancos de dados
* Escolha baseada no tipo de dado
* Integração entre tecnologias
* Aplicação de arquitetura moderna

---

## Considerações Finais

Este projeto prioriza:

* Simplicidade do modelo relacional
* Separação clara de responsabilidades entre bancos
* Performance e escalabilidade
