
# 📚 Catálogo de Trabalhos Acadêmicos e Projetos
## 👥 Autores
* Felipe
* Kauan
* Wellyson
* Pedro
* Lamborghini

## 📖 Descrição

Este projeto consiste em um **catálogo digital de trabalhos acadêmicos e projetos desenvolvidos por estudantes**, permitindo que novas turmas possam **se inspirar em produções passadas, consultar ideias, registrar novas criações e evitar a perda ou a cópia de trabalhos antigos**.

A plataforma promove a **organização, preservação e reutilização de conhecimento** produzido em ambiente acadêmico.

---

## 🎯 Objetivos

* Disponibilizar um repositório acessível de projetos e trabalhos acadêmicos.
* Permitir que estudantes cadastrem seus próprios projetos.
* Facilitar a pesquisa de trabalhos já cadastrados.
* Evitar a duplicação ou cópia de trabalhos antigos.
* Servir como fonte de inspiração para novos projetos.

---

## ⚙️ Funcionalidades

* **Cadastro de usuário** com nome, e-mail, senha e foto de perfil.
* **Login de usuário** para acesso ao sistema.
* **Registro de projetos** com título, descrição, autores e data de publicação.
* **Pesquisa de projetos** por título ou descrição.
* **Visualização de projetos** com detalhes.
* **Favoritar projetos** para consulta rápida.
* **Gerenciamento administrativo** com permissões para editar ou excluir projetos.

---

## 🗂️ Estrutura do Sistema

### Entidades principais:

* **Usuário** → responsável por cadastrar e favoritar projetos.
* **Projeto** → trabalhos cadastrados com título, descrição, autores e data.
* **Autor_Projeto** → relacionamento entre usuários e projetos.
* **Favorito** → permite que projetos sejam salvos pelos usuários.

---

## 🛠️ Tecnologias Utilizadas

* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python (Flask/Django) ou Node.js (dependendo da implementação escolhida)
* **Banco de Dados:** MySQL / PostgreSQL
* **Controle de Versão:** Git e GitHub
* **Ferramentas:** Visual Studio Code

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:

   bash
   git clone https://github.com/seu-usuario/catalogo-projetos.git

2. Acesse o diretório do projeto:

   bash
   cd catalogo-projetos
   
3. Configure o ambiente virtual (Python) ou instale as dependências do Node.js.

   bash
   pip install -r requirements.txt   # para Python  
   npm install                      # para Node.js
   
4. Execute o servidor:

   bash
   python app.py      # para Flask/Django  
   npm start          # para Node.js
   
5. Abra o navegador em:

   
   http://localhost:3000



## 📌 Possíveis Expansões Futuras

* Sistema de verificação de plágio.
* Upload de arquivos (PDF, imagens, relatórios).
* Comentários e avaliações em projetos.
* Integração com APIs educacionais.
* Módulo de estatísticas de acesso e popularidade.