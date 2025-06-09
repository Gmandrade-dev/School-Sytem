# 🏫 Sistema Escolar - Python + CustomTkinter + PostgreSQL

Este é um sistema escolar desenvolvido em **Python**, com interface gráfica usando **CustomTkinter**, banco de dados **PostgreSQL** e arquitetura **MVC** (Model-View-Controller). O sistema possui autenticação para dois tipos de usuários: **alunos** e **professores**, com funcionalidades específicas para cada perfil, facilitando o gerenciamento acadêmico.

---

## ✨ Funcionalidades

### 👨‍🎓 Aluno

* Login com autenticação
* Visualização das **notas**
* Edição do **perfil**

### 👨‍🏫 Professor

* Painel administrativo completo
* **Cadastro**, **edição** e **exclusão** de:

  * Alunos
  * Professores
  * Disciplinas
  * Notas
* Consulta de usuários por número de **matrícula**
* Visualização completa de todos os registros

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Banco de Dados:** PostgreSQL
* **Arquitetura:** MVC (Model-View-Controller)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   git clone https://github.com/Gmandrade-dev/School-Sytem.git
   cd seu-repositorio

2. **Instale as dependências:**
   pip install customtkinter psycopg2

3. **Configurações iniciais:**

   * Abra o arquivo `cnx.py` dentro da pasta `model` e ajuste as configurações do PostgreSQL para o seu ambiente local (host, usuário, senha, banco de dados).
   * Execute o arquivo `criacao.py` para criar o banco de dados, as tabelas e inserir os dados padrões:
     python criacao.py

4. **Inicie o sistema:**
   python main.py

---

## 👨‍🏫 Visão de Professor (para testes)

* **Usuário:** admin
* **Senha:** 123

---

Se precisar de ajuda com qualquer etapa, fique à vontade para abrir uma issue ou entrar em contato!
