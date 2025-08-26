# WorkoutAPI

Oi! Essa é a **WorkoutAPI**, para você gerenciar atletas, categorias e centros de treinamento de forma prática e organizada.

---

## Autora

**Ana Bárbara Marques dos Santos** – estudante de Engenharia de Software 💜

---

## 🚀 Como rodar a API

1. Criar e ativar o ambiente virtual:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

Instalar as dependências:
pip install -r requirements.txt

Rodar a API:
python -m uvicorn main:app --reload

Acessar a documentação interativa
http://127.0.0.1:8000/docs

✨ Endpoints principais
GET /atletas/ — listar atletas (com filtros de nome, cpf e paginação)

POST /atletas/ — criar atleta novo

GET /categorias/ — listar categorias

POST /categorias/ — criar categoria nova

GET /centros/ — listar centros de treinamento

POST /centros/ — criar centro novo

💡 Observações
O banco de dados usado é PostgreSQL.
Lembre-se de ignorar a pasta venv/ no Git.
Divirta-se testando a API e explorando os endpoints! 🎉
Lembre-se de ignorar a pasta venv/ no Git.

Divirta-se testando a API e explorando os endpoints! 🎉
