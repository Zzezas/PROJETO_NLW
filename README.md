Sistema de Inscrição de Eventos com Links de Indicação (API Backend)
<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python 3.9+">
<img src="https://img.shields.io/badge/Flask-2.2%2B-green?style=for-the-badge&logo=flask" alt="Flask">
<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status: Em Desenvolvimento">
</p>

📖 Sobre o Projeto
Este é o repositório do backend de um Sistema de Inscrição de Eventos. O principal objetivo deste projeto é fornecer uma API robusta e funcional para gerenciar inscrições de participantes em eventos, com um diferencial: um sistema de links de indicação.

Este projeto foi desenvolvido como parte do meu portfólio pessoal para demonstrar minhas habilidades em desenvolvimento backend com Python e Flask, criação de APIs RESTful e integração com banco de dados.

O próximo passo é a construção de uma interface front-end para consumir esta API, criando uma experiência de usuário completa e visualmente agradável.

✨ Funcionalidades Principais
Criação de Eventos: Endpoints para cadastrar novos eventos no sistema.

Inscrição de Pessoas: Permite que usuários se inscrevam em um evento específico.

Geração de Links de Indicação: Cada pessoa inscrita recebe um link único para indicar novos participantes.

Listagem e Detalhamento: Rotas para listar todos os eventos, buscar um evento específico e ver os participantes inscritos.

Validações: O sistema valida os dados recebidos para garantir a integridade das informações.

🛠️ Tecnologias Utilizadas
Este projeto foi construído utilizando as seguintes tecnologias e ferramentas:

Python: Linguagem de programação principal do projeto.

Flask: Micro-framework web para a criação da API, gerenciamento de rotas e do servidor.

Postman: Ferramenta utilizada para testar e documentar os endpoints da API durante o desenvolvimento.

DBeaver: Cliente de banco de dados universal, utilizado para gerenciar e visualizar os dados do projeto.

Banco de Dados (Ex: SQLite, PostgreSQL): [Descreva aqui o banco de dados que você usou, por exemplo: "SQLite para simplicidade em desenvolvimento"].

🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

Pré-requisitos
Python 3.9 ou superior

pip (gerenciador de pacotes do Python)

Instalação
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual:

Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
(Nota: Certifique-se de ter um arquivo requirements.txt com todas as bibliotecas, como o Flask. Para criá-lo, use o comando pip freeze > requirements.txt)

Executando o Servidor
Com as dependências instaladas, inicie o servidor Flask:

Bash

flask run
O servidor estará rodando em http://127.0.0.1:5000.

🔌 Como Usar a API
Você pode usar o Postman ou outra ferramenta de sua preferência para interagir com a API.

Exemplos de Endpoints
1. Inscrever uma pessoa em um evento
Método: POST

URL: http://127.0.0.1:5000/inscricao

Corpo da Requisição (JSON):

JSON

{
    "nome_pessoa": "João da Silva",
    "email": "joao.silva@example.com",
    "id_evento": 1
}
Resposta de Sucesso (201 Created):

JSON

{
    "mensagem": "Inscrição realizada com sucesso!",
    "link_indicacao": "http://127.0.0.1:5000/indicacao/abcdef123"
}
2. Listar todos os eventos
Método: GET

URL: http://127.0.0.1:5000/eventos

🔮 Próximos Passos (Roadmap)
[ ] Desenvolvimento do Front-end: Criar uma interface web bonita e responsiva (provavelmente com React, Vue ou Angular) para consumir esta API.

[ ] Sistema de Autenticação: Implementar autenticação de usuários (JWT - JSON Web Tokens) para proteger rotas.

[ ] Contagem de Indicações: Desenvolver a lógica para contabilizar quantas pessoas se inscreveram através de cada link de indicação.

[ ] Testes Automatizados: Escrever testes unitários e de integração para garantir a qualidade e estabilidade do código.

[ ] Deploy: Publicar a aplicação em um serviço de nuvem como Heroku, Vercel ou AWS.

👨‍💻 Autor
Feito com ❤️ por [Seu Nome]

LinkedIn: https://www.linkedin.com/in/seu-linkedin/

GitHub: https://github.com/seu-usuario/

✅ Automatizar envio de convites por e-mail

✅ Front-end

📌 Feito com dedicação e Python puro 🐍.




