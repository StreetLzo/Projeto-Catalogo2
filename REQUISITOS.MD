# Documento de Requisitos – Catálogo de Trabalhos Acadêmicos

**Disciplinas:** Programação Web, Projeto e Desenvolvimento de Sistemas, Banco de Dados II

**Alunos:** Felipe, Kauan, Wellyson, Pedro, Lamborghini

**Professores:** Camila Santos, Eudóxia Moura, Marcos Faino

---

## 📖 Descrição Geral do Sistema

O **Catálogo de Trabalhos Acadêmicos e Projetos** tem como objetivo armazenar, organizar e disponibilizar projetos desenvolvidos por estudantes, permitindo a consulta de trabalhos de turmas anteriores, favorecendo a preservação do conhecimento, a inspiração para novas ideias e a prevenção da duplicação de conteúdos.

O sistema permite que usuários registrem novos projetos, pesquisem, visualizem, favoritem e façam download dos arquivos associados. Professores e administradores podem gerenciar os registros e manter a integridade dos dados.

---

## 🔎 Pesquisa Desk

O levantamento de requisitos foi realizado por meio de:

* Conversas com professores e alunos sobre necessidades acadêmicas.
* Análise de repositórios similares em universidades.
* Identificação de problemas atuais, como:

  * Perda de trabalhos por falta de centralização.
  * Dificuldade de consulta a projetos antigos.
  * Risco de plágio ou repetição de ideias.

---

## 👥 Atores / Personas

* **Visitante:** Pode pesquisar e visualizar trabalhos, mas não cadastrar.
* **Aluno/Usuário Registrado:** Pode cadastrar-se, fazer login, registrar projetos, pesquisar, visualizar e favoritar projetos.
* **Administrador:** Possui permissões avançadas para editar e excluir projetos e gerenciar usuários.
* **Professor:** Atua como avaliador e pode acessar relatórios de uso ou projetos cadastrados.

---

## ✅ Requisitos Funcionais (Casos de Uso)

* Permitir cadastro, login e logout de usuários.
* Registrar novos projetos com título, descrição, autores e arquivo anexo.
* Editar e excluir projetos (apenas autores ou administradores).
* Pesquisar projetos por título, descrição ou autor.
* Visualizar detalhes de projetos cadastrados.
* Favoritar projetos para acesso rápido.
* Listar projetos recentes e mais populares.
* Permitir que administradores gerenciem usuários.
* Possibilidade de download dos arquivos anexados.
* Exibir histórico dos projetos cadastrados.

---

## ⚙️ Requisitos Não Funcionais

* **Interface amigável e responsiva**, utilizando Bootstrap.
* **Autenticação segura** (criptografia de senhas, controle de sessão).
* **Disponibilidade** contínua para acesso acadêmico.
* **Compatibilidade** com desktop e dispositivos móveis.
* **Banco de dados relacional** (SQLite em desenvolvimento, MySQL em produção).
* **Backup automático** dos dados em produção.
* **Tempo de resposta** inferior a 3 segundos por operação.
* **Organização modular** para permitir manutenção e evolução do sistema.

---

## 📚 Referências

* Documentação oficial do Flask e Flask-SQLAlchemy.
* Projetos similares de catálogos acadêmicos em universidades.
* Sites de repositórios open source.
* Materiais de aula de Banco de Dados II, Programação Web e PDS.
