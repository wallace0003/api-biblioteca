# 📚 Sistema de Biblioteca

Este projeto consiste no desenvolvimento de um **Sistema de Gerenciamento de Biblioteca** utilizando uma arquitetura de **persistência poliglota**, ou seja, o uso de diferentes bancos de dados dentro de uma mesma aplicação, cada um com uma responsabilidade específica.

O objetivo do sistema é permitir o gerenciamento de informações relacionadas a uma biblioteca, como o cadastro de livros, autores, usuários e empréstimos, além de registrar logs da aplicação e melhorar o desempenho por meio de cache.

---

## 🎯 Tema escolhido

O tema escolhido para este projeto foi um **Sistema de Biblioteca**.

A escolha desse tema se justifica por ser um cenário comum em aplicações reais, envolvendo diferentes tipos de dados e relacionamentos. Em uma biblioteca, é necessário controlar informações estruturadas, como usuários, livros, autores e empréstimos, além de lidar com dados de consulta frequente e registros de atividades do sistema.

Esse contexto permite aplicar de forma prática o conceito de **persistência poliglota**, utilizando o banco de dados mais adequado para cada tipo de informação.

---

## 🏗️ Arquitetura do Projeto

A aplicação utiliza três tecnologias principais de persistência:

- **PostgreSQL**: banco de dados relacional;
- **Redis**: sistema de cache;
- **MongoDB**: banco de dados NoSQL orientado a documentos.

Cada banco possui uma função específica dentro do sistema, contribuindo para melhor organização, desempenho e escalabilidade da aplicação.

---

## 🧩 Modelo Relacional

O banco relacional da aplicação é representado por entidades como autores, livros, usuários e empréstimos.

A imagem abaixo representa o modelo relacional do sistema:

<img width="946" height="513" alt="mer_biblioteca drawio" src="https://github.com/user-attachments/assets/ad5bfb71-1b9b-4c27-84a5-1bb69df7f1c9" />


---

## 🐘 PostgreSQL

O **PostgreSQL** é utilizado como banco de dados relacional principal do sistema.

Ele é responsável por armazenar os dados estruturados da aplicação, garantindo integridade, consistência e relacionamento entre as entidades principais.

No projeto, o PostgreSQL armazena informações como:

- Autores;
- Livros;
- Usuários;
- Empréstimos;
- Relacionamentos entre livros, autores e usuários.

A escolha do PostgreSQL se justifica porque os dados principais da biblioteca possuem estrutura bem definida e relacionamentos importantes. Por exemplo, um livro pertence a um autor, um empréstimo está associado a um usuário e também a um livro.

O uso de um banco relacional permite aplicar chaves primárias, chaves estrangeiras e regras de integridade, garantindo maior confiabilidade nos dados armazenados.

---

## 🗃️ Tabelas necessárias no PostgreSQL

Para o funcionamento correto da aplicação, é necessário que o banco PostgreSQL possua as tabelas descritas abaixo.

---

### Tabela `authors`

A tabela `authors` é responsável por armazenar os autores dos livros cadastrados no sistema.

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id_author` | Integer | Sim | Chave primária do autor |
| `author_name` | String(60) | Sim | Nome do autor |

#### Relacionamento

- Um autor pode possuir vários livros cadastrados;
- O relacionamento com a tabela `books` ocorre por meio do campo `id_author`.

---

### Tabela `books`

A tabela `books` é responsável por armazenar os livros disponíveis na biblioteca.

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id_book` | Integer | Sim | Chave primária do livro |
| `title` | String(100) | Sim | Título do livro |
| `year` | Integer | Não | Ano de publicação do livro |
| `id_author` | Integer | Sim | Chave estrangeira que referencia `authors.id_author` |

#### Relacionamentos

- Um livro pertence a um autor;
- Um livro pode estar associado a vários empréstimos;
- O campo `id_author` cria o relacionamento com a tabela `authors`.

---

### Tabela `loans`

A tabela `loans` é responsável por armazenar os empréstimos de livros realizados pelos usuários.

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id_loan` | Integer | Sim | Chave primária do empréstimo |
| `id_user` | Integer | Sim | Chave estrangeira que referencia `users.id_user` |
| `id_book` | Integer | Sim | Chave estrangeira que referencia `books.id_book` |
| `created_at` | DateTime | Sim | Data e hora de criação do registro |
| `date_loan` | Date | Sim | Data em que o empréstimo foi realizado |
| `date_return` | Date | Não | Data em que o livro foi devolvido |
| `date_expected_return` | Date | Não | Data prevista para devolução do livro |

#### Relacionamentos

- Um empréstimo pertence a um usuário;
- Um empréstimo está relacionado a um livro;
- O campo `id_user` referencia a tabela `users`;
- O campo `id_book` referencia a tabela `books`.

> Observação: como a tabela `loans` possui uma chave estrangeira para `users.id_user`, também é necessário que exista uma tabela `users` no banco PostgreSQL para representar os usuários do sistema.

---

## ⚡ Redis

O **Redis** é utilizado como sistema de cache da aplicação.

Ele armazena temporariamente informações acessadas com frequência, como dados de livros e consultas recorrentes. Dessa forma, evita que a aplicação precise consultar o PostgreSQL repetidamente para buscar as mesmas informações.

A escolha do Redis se justifica por sua alta performance e baixa latência, sendo uma solução adequada para otimizar o tempo de resposta da aplicação.

No projeto, o Redis contribui para:

- Melhorar o desempenho das consultas;
- Reduzir a carga sobre o PostgreSQL;
- Acelerar o acesso a dados frequentemente utilizados;
- Tornar a aplicação mais eficiente.

---

## 🍃 MongoDB

O **MongoDB** é utilizado para armazenar dados semi-estruturados.

Neste projeto, ele é responsável principalmente pelo armazenamento de logs da aplicação, como registros de operações, eventos internos, erros e ações realizadas no sistema.

A escolha do MongoDB se justifica porque logs podem possuir estruturas diferentes dependendo do tipo de evento registrado. Como o MongoDB é um banco NoSQL orientado a documentos, ele permite armazenar essas informações de forma flexível, sem a necessidade de uma estrutura rígida como em um banco relacional.

No projeto, o MongoDB contribui para:

- Armazenar logs da aplicação;
- Facilitar futuras análises e auditorias;
- Permitir flexibilidade na estrutura dos dados;
- Separar os registros de eventos dos dados principais do sistema.

---

## 🧠 Definição da implementação do backend

O backend será implementado em **Python**, utilizando uma estrutura organizada em camadas para facilitar a manutenção e evolução do projeto.

A aplicação será responsável por centralizar as regras de negócio do sistema de biblioteca, realizar a comunicação com os bancos de dados e disponibilizar as funcionalidades necessárias para o gerenciamento dos dados.

O backend deverá contemplar:

- Cadastro e consulta de autores;
- Cadastro e consulta de livros;
- Cadastro e consulta de usuários;
- Registro de empréstimos;
- Registro de devoluções;
- Consulta de livros disponíveis;
- Utilização de cache com Redis;
- Registro de logs no MongoDB;
- Persistência dos dados principais no PostgreSQL.

Para comunicação com o PostgreSQL, será utilizado o **SQLAlchemy**, realizando o mapeamento das entidades do sistema por meio de modelos ORM.

A responsabilidade de cada serviço no backend será dividida da seguinte forma:

| Serviço | Responsabilidade |
|---|---|
| Backend Python | Implementar as regras de negócio e expor as funcionalidades da aplicação |
| PostgreSQL | Armazenar dados relacionais e estruturados |
| Redis | Armazenar dados temporários em cache |
| MongoDB | Armazenar logs e dados semi-estruturados |

---

## 📌 Resumo da persistência poliglota

A aplicação utiliza uma arquitetura de persistência poliglota para aproveitar os pontos fortes de cada tecnologia.

| Tecnologia | Tipo | Função no sistema |
|---|---|---|
| PostgreSQL | Relacional | Armazenamento dos dados principais da biblioteca |
| Redis | Cache em memória | Otimização de consultas e melhoria de performance |
| MongoDB | NoSQL orientado a documentos | Armazenamento de logs e dados semi-estruturados |

Essa abordagem permite que cada tipo de dado seja armazenado na tecnologia mais adequada, tornando o sistema mais organizado, performático e escalável.

---

## 🚀 Como executar o projeto

Para executar o projeto localmente, é necessário ter os seguintes pré-requisitos instalados na máquina:

- Docker;
- Docker Compose;
- Python.

---

### 1. Iniciar os serviços com Docker

Na raiz do projeto, execute o comando abaixo para iniciar os containers dos serviços utilizados pela aplicação, como PostgreSQL, Redis e MongoDB:

```bash
docker-compose up
```

Ou, dependendo da versão instalada do Docker Compose:

```bash
docker compose up
```

Caso seja necessário reconstruir as imagens dos containers, utilize:

```bash
docker compose up --build
```

> Mantenha os containers em execução enquanto estiver utilizando a aplicação.

---

### 2. Criar o ambiente virtual Python

Com os serviços iniciados, crie um ambiente virtual para instalar as dependências do projeto:

```bash
python -m venv .venv
```

---

### 3. Ativar o ambiente virtual

No **Windows**, execute:

```bash
.venv\Scripts\activate
```

No **Linux** ou **macOS**, execute:

```bash
source .venv/bin/activate
```

---

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

### 5. Executar a aplicação

Após instalar as dependências, execute a aplicação com o comando:

```bash
python -m app.main
```

---

### Resumo dos comandos

```bash
docker compose up
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

> No Windows, substitua o comando de ativação do ambiente virtual por:

```bash
.venv\Scripts\activate
```

---

## ⚙️ Serviços utilizados

Ao executar o projeto com Docker Compose, os seguintes serviços devem ser iniciados:

| Serviço | Descrição |
|---|---|
| `backend` | Serviço principal da aplicação |
| `postgres` | Banco de dados relacional PostgreSQL |
| `redis` | Serviço de cache Redis |
| `mongodb` | Banco de dados NoSQL MongoDB |

Esses serviços trabalham em conjunto para permitir o funcionamento completo da aplicação.

---

## 🧪 Fluxo geral da aplicação

O funcionamento esperado da aplicação ocorre da seguinte forma:

1. O usuário realiza uma operação no sistema, como cadastrar um livro ou registrar um empréstimo;
2. O backend recebe a requisição e aplica as regras de negócio;
3. Os dados principais são salvos ou consultados no PostgreSQL;
4. Informações acessadas com frequência podem ser armazenadas no Redis para melhorar o desempenho;
5. Eventos importantes da aplicação são registrados no MongoDB em formato de logs.

---

## ✅ Tecnologias utilizadas

- Python;
- SQLAlchemy;
- PostgreSQL;
- Redis;
- MongoDB;
- Docker;
- Docker Compose.

---

## 📖 Considerações finais

Este projeto demonstra a aplicação prática do conceito de persistência poliglota em um sistema de biblioteca.

A utilização de PostgreSQL, Redis e MongoDB permite separar responsabilidades de armazenamento, melhorar a performance da aplicação e tornar o sistema mais flexível para futuras expansões.

Com essa arquitetura, o projeto consegue lidar de forma adequada com dados relacionais, informações em cache e registros semi-estruturados, aplicando cada tecnologia no contexto em que ela oferece melhores benefícios.
