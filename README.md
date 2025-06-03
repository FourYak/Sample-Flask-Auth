
## 🔐 Flask Auth API - Sistema de Autenticação e CRUD de Usuários
Um projeto Flask completo com sistema de autenticação segura e operações CRUD para gerenciamento de usuários, desenvolvido como parte do módulo de aprendizagem Python.

### ✨ Funcionalidades Principais
Autenticação segura com hash de senhas usando bcrypt

Sistema de login/logout com sessões protegidas

CRUD completo (Create, Read, Update, Delete) de usuários

Controle de acesso baseado em roles (usuário/admin)

API RESTful com respostas em JSON

### 🛠️ Tecnologias Utilizadas
Flask - Framework web Python

Flask-Login - Gerenciamento de sessões de usuário

SQLAlchemy - ORM para banco de dados

MySQL - Banco de dados relacional

bcrypt - Criptografia de senhas

### ⚙️ Configuração do Projeto
#### Pré-requisitos:

Python 3.8+

MySQL instalado

Pip para instalação de dependências

Instalação:

bash
git clone https://github.com/.../.git
cd flask-auth-api
pip install -r requirements.txt
Configuração do Banco de Dados:

Crie um banco MySQL chamado flask-crud

Altere as credenciais no arquivo de configuração conforme necessário

Execução:

bash
python app.py
### 📚 Endpoints da API
### 🔑 Autenticação
POST /login - Faz login com username e password

GET /logout - Encerra a sessão do usuário

### 👥 Gerenciamento de Usuários
POST /user - Cria um novo usuário

GET /user/<id> - Obtém informações de um usuário

PUT /user/<id> - Atualiza um usuário

DELETE /user/<id> - Remove um usuário (apenas admin)

### 🧪 Teste
GET /hello-world - Rota de teste simples

### 🔒 Segurança Implementada
Hash de senhas com bcrypt antes de armazenar no banco

Proteção de rotas com @login_required

Controle de acesso baseado em roles (usuário/admin)

Sessões seguras com Flask-Login

Validação de dados em todas as entradas

### 🚀 Como Contribuir
Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/incrivel)

Commit suas mudanças (git commit -m 'Adicionando feature incrível')

Push para a branch (git push origin feature/incrivel)

Abra um Pull Request


Desenvolvido com dedicação por Maik Quebra como parte do curso Python 100h da Rocketseat.