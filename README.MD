
## 📄 README.md

````markdown
# 📚 Catálogo de Trabalhos Acadêmicos

Este projeto tem como objetivo oferecer uma plataforma simples e eficiente para o **cadastro, organização e consulta de projetos acadêmicos**, permitindo que estudantes e professores tenham acesso a trabalhos de turmas anteriores, evitando a perda de conhecimento e incentivando a inovação.

---

## 🚀 Funcionalidades

- Cadastro de usuários  
- Autenticação segura (login/logout)  
- Cadastro de projetos com título, descrição, autores e arquivo anexo  
- Pesquisa de projetos por título, descrição ou autor  
- Favoritar projetos para consulta rápida  
- Edição e exclusão de projetos (autores e administradores)  
- Painel administrativo para gerenciar usuários e projetos  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**  
- **Flask** (framework web)  
- **Flask-WTF** (formulários e validação)  
- **Flask-Login** (autenticação)  
- **Flask-Migrate + SQLAlchemy** (ORM e migrações de banco)  
- **SQLite** (banco padrão, podendo trocar para MySQL)  
- **Bootstrap 5** (frontend responsivo)  

---

## 📂 O que você encontra aqui

Neste repositório você encontrará:  
- Código-fonte completo da aplicação  
- Estrutura de templates HTML com Bootstrap  
- Arquivo `requirements.txt` com dependências do projeto  
- Documentação básica para rodar o sistema localmente  

---

## ▶️ Como executar o projeto

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/catalogo-projetos.git
   cd catalogo-projetos
````

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:

   ```bash
   flask db init
   flask db migrate -m "initial"
   flask db upgrade
   ```

5. Rode a aplicação:

   ```bash
   flask run
   ```

6. Acesse no navegador:

   ```
   http://127.0.0.1:5000
   ```

---

## 👥 Autores

* Felipe
* Kauan
* Lamborghini

```
