# ⚡ Zuplae Python Starter

Boilerplate moderno da **Zuplae** para projetos em Python com **FastAPI**, configurado com **Poetry**, qualidade de código (Ruff, Black, mypy), testes automatizados, Docker e CI no GitHub Actions.

---

## 🚀 Tecnologias e ferramentas

* **Linguagem:** Python 3.13
* **Framework Web:** FastAPI + Uvicorn/Gunicorn
* **Gerenciamento de dependências:** Poetry
* **Configurações e envs:** pydantic-settings
* **Qualidade de código:** Ruff, Black, mypy, pre-commit
* **Testes:** pytest, pytest-asyncio, httpx
* **Containerização:** Docker e Docker Compose
* **CI/CD:** GitHub Actions

---

## 📂 Estrutura do projeto

```
📦 zuplae-python-starter/
├── app/                  # Código principal
│   ├── api/               # Rotas
│   ├── core/              # Configurações e logging
│   └── main.py             # Entrada da aplicação
├── tests/                 # Testes unitários
├── .env.example           # Exemplo de variáveis de ambiente
├── docker-compose.yml     # Serviços Docker
├── Dockerfile             # Build da aplicação
├── Makefile               # Comandos úteis
└── pyproject.toml         # Configuração do Poetry
```

---

## 🧪 Começo rápido

### 1. Clonar e instalar dependências

```bash
git clone git@github.com:ZuplaeSistemas/zuplae-python-starter.git
cd zuplae-python-starter
poetry install
cp devtools/envs/.env.example .env
poetry run pre-commit install
```

### 2. Rodar em desenvolvimento

```bash
poetry run app
# Acesse http://localhost:8000/docs
```

### 3. Rodar com Docker

```bash
docker compose up --build
```

---

## 🛠️ Scripts úteis (Makefile)

* `make init` → instala deps, copia .env e configura pre-commit
* `make run` → inicia a API em modo dev
* `make lint` → checa código com Ruff
* `make format` → formata código com Black e Ruff
* `make type` → verifica tipagem com mypy
* `make test` → executa testes
* `make docker-up` / `make docker-down` → sobe ou derruba containers

---

## 📋 Teste de saúde

```bash
curl http://localhost:8000/api/v1/health
# {"status":"ok"}
```

---

## 📦 CI/CD

O projeto já inclui um **GitHub Actions** que:

1. Instala dependências
2. Roda lint e format check
3. Executa verificação de tipos (mypy)
4. Roda todos os testes

---

## 📜 Licença

Este projeto é mantido pela **Zuplae** e segue os termos definidos internamente.
