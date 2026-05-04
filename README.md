# 📚 Sistema de Biblioteca

Este projeto consiste no desenvolvimento de um sistema de gerenciamento de biblioteca utilizando uma arquitetura poliglota de persistência.

A aplicação foi projetada para utilizar diferentes tipos de bancos de dados, cada um com uma responsabilidade específica, visando melhor desempenho, escalabilidade e organização dos dados.

## 🏗️ Arquitetura

O sistema utiliza múltiplos bancos de dados, cada um escolhido de acordo com sua finalidade:

- Banco relacional para dados estruturados
- Banco NoSQL para dados semi-estruturados
- Sistema de cache para otimização de performance

## 🚀 Como executar o projeto

Para executar o projeto, é necessário ter o Docker e o Docker Compose instalados na máquina.

Utilize o comando abaixo para iniciar os containers:

```bash
docker-compose up
```
---

## 🐘 PostgreSQL

O PostgreSQL é utilizado como banco de dados relacional do sistema.

Ele é responsável por armazenar dados estruturados e garantir a integridade das informações, como:

- Usuários
- Empréstimos
- Relacionamentos entre entidades

Esse modelo segue o padrão relacional, garantindo consistência e organização dos dados principais da aplicação.

## ⚡ Redis

O Redis é utilizado como sistema de cache.

Ele armazena informações que são frequentemente acessadas pelos usuários, como os dados dos livros, melhorando significativamente o desempenho da aplicação e reduzindo a carga sobre o banco de dados principal.

## 🍃 MongoDB

O MongoDB é utilizado para armazenar dados semi-estruturados.

Neste projeto, ele é responsável principalmente pelo armazenamento de logs do sistema, permitindo maior flexibilidade na estrutura dos dados e facilitando análises futuras.
