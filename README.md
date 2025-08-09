📋 Event Registration Backend
<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python 3.9+">
<img src="https://img.shields.io/badge/Flask-2.2%2B-green?style=for-the-badge&logo=flask" alt="Flask">
<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status: Em Desenvolvimento">
</p>

Um sistema backend completo em Python para gerenciar inscrições de pessoas em eventos, com links de indicação, pronto para ser integrado a um futuro front-end.

🚀 Sobre o projeto
Este projeto foi desenvolvido como um exemplo prático para meu portfólio.
A aplicação é responsável por:

Criar rotas com Flask para gerenciar eventos e inscrições.

Receber e enviar dados via API (testada no Postman).

Armazenar informações no banco de dados, manipulado pelo DBeaver.

Suportar links de indicação para cada inscrição.

Servir como base para integração futura com um site completo.

O próximo passo será criar um front-end bonito e responsivo para exibir tudo em tempo real.

✨ Funcionalidades
📌 Cadastro de eventos

📝 Inscrição de participantes

🔗 Geração de links de indicação únicos

📊 Listagem e consulta de dados

🗄️ Integração com banco de dados

🛠 Tecnologias utilizadas
Python 3

Flask

Postman (para testes de API)

DBeaver (para gerenciamento do banco)

SQLite / PostgreSQL (dependendo do ambiente)

📦 Como executar
Clone o repositório

bash
Copiar
Editar
git clone https://github.com/seuusuario/nome-do-repositorio.git
Acesse a pasta

bash
Copiar
Editar
cd nome-do-repositorio
Crie um ambiente virtual

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt
Execute o servidor

bash
Copiar
Editar
python app.py
Teste no Postman usando http://localhost:5000/

📌 Próximos passos
Criar interface web para inscrições (front-end com HTML, CSS, JavaScript e frameworks modernos).

Melhorar autenticação e segurança.

Implementar estatísticas e relatórios.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

💡 Este projeto faz parte do meu portfólio de desenvolvimento. Feedbacks são bem-vindos! 🚀
