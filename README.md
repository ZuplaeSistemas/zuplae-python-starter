# 📊 Zuplae Python Starter

O **Zuplae Python Starter** é um boilerplate para criação de APIs modernas com **FastAPI**, estruturado para seguir boas práticas de arquitetura, logging, configuração, linting e testes automatizados.

---

## 🚀 **Tecnologias Utilizadas**

* **Linguagem:** Python 3.13+
* **Framework:** FastAPI
* **Validação e Configuração:** Pydantic + Pydantic Settings
* **Logs:** Configuração centralizada com suporte a formatação customizada e contextos
* **Testes:** Pytest + HTTPX
* **Dependências:** Poetry
* **Lint & Formatação de Código:** Black + Ruff + Mypy + Pre-commit

---

## 🛠️ **Estrutura do Projeto**

```
app/
├── api/                     # Endpoints da aplicação
│   └── v1/                  # Versão da API
│       ├── health/          # Exemplo de rota de health check
│       │   ├── controller.py
│       │   ├── schema.py
│       │   └── __init__.py
├── core/                    # Configurações centrais
│   ├── config.py             # Configurações via Pydantic Settings
│   ├── deps.py               # Injeção de dependências
│   └── logging.py            # Configuração de logging
├── domains/                  
│   └── health/
│       ├── use_case.py       # Regras de negócio
|       └──repositories/      # Camada de acesso a dados
├── main.py                   # Entrypoint FastAPI
└── app.py                    # Função `create_app`

devtools/                     # Ferramentas e scripts auxiliares
Makefile                      # Comandos de automação
pyproject.toml                # Configurações do Poetry e ferramentas
```

---

## 🔧 **Configuração de Logs**

Logs centralizados no `app/core/logging.py` com suporte a contexto extra via `extra={}`.

```python
from app.core.logging import get_logger
logger = get_logger(__name__)
logger.info("get liveness", extra={"context": "health"})
```

---

## 📓 **Makefile**

Comandos úteis:

```bash
make run           # Executa a aplicação localmente
make test          # Executa os testes
make lint          # Verifica estilo do código (black, ruff e mypy)
make format-check  # Checa a formacacao do código (black e ruff --check)
make format        # Formata código (black e ruff --fix)
make pre-commit:   # Faz o check manual do pre-commit
make install       # Instala dependências
```

---

## 🔍 **Lint & Pre-commit**

O projeto utiliza **Black**, **Ruff** e **Mypy** para lint, formatação e checagem de tipos.

* **Black** → Formatação consistente de código.
* **Ruff** → Linter ultrarrápido e substituto do isort.
* **Mypy** → Checagem estática de tipos.

Configuração do **pre-commit** (`.pre-commit-config.yaml`):

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.2
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
```

Instalação dos hooks:

```bash
poetry run pre-commit install
```

Execução manual:

```bash
make pre-commit
```

---

## 🗂 **API, Domains e Repository**

* **`api/vx`**: Camada de entrega (controllers)
* **`domains`**: Casos de uso / regra de negócio
* **`repositories`**: Acesso a dados

Fluxo sugerido:

```
Request -> Controller (api/vx) -> UseCase (domains) -> Repository -> Resposta
```

---

## 🛠️ **Rodando o Projeto**

```bash
# Clone do repositorio
git clone git@github.com:ZuplaeSistemas/zuplae-python-starter.git

# Acessar o repositorio local
cd zuplae-python-starter

# Usar o pyenv para usar a versão correta do Python
pyenv global 3.13.2

# Instalar o poetry
pip install poetry

# Instalar dependências do projeto
poetry install

# Ativar virtualenv
eval $(poetry env activate)

# Criar .env a partir da env exemplo
cp devtools/envs/.env.dev .env

# Rodar aplicação
make run
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📚 **Testes**

Testes assíncronos com pytest e HTTPX.

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(base_url="http://test") as ac:
        response = await ac.get("/api/v1/health/liveness")
    assert response.status_code == 200
```

### Rodando os testes

Os testes utilizam um arquivo `.env.test` específico (em `devtools/envs/.env.test`).
O comando do Makefile já cuida de copiar esse arquivo para `.env` antes de rodar os testes:

```bash
make test
```

---

## 🔍 **Próximos Passos**

* [ ] Adicionar novos casos de uso
* [ ] Criar repositórios reais
* [ ] Configurar CI/CD
* [ ] Implementar autenticação JWT
