# 📊 Zuplae Python Starter

O **Zuplae Python Starter** é um boilerplate para criação de APIs modernas com **FastAPI**, estruturado para seguir boas práticas de arquitetura, logging, configuração e testes automatizados.

---

## 🚀 **Tecnologias Utilizadas**

* **Linguagem:** Python 3.13+
* **Framework:** FastAPI
* **Validação e Configuração:** Pydantic + Pydantic Settings
* **Logs:** Configuração centralizada com suporte a formatação customizada e contextos
* **Testes:** Pytest + HTTPX
* **Dependências:** Poetry
* **Formatação de Código:** Black + Ruff + isort

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
make run         # Executa a aplicação localmente
make test        # Executa os testes
make lint        # Verifica estilo do código
make format      # Formata código
make install     # Instala dependências
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
# Instalar dependências
poetry install

# Ativar virtualenv
eval $(poetry env activate)

# Criar .env
cp devtools/envs/.env.example .env

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

---

## 🔍 **Próximos Passos**

* [ ] Adicionar novos casos de uso
* [ ] Criar repositórios reais
* [ ] Configurar CI/CD
* [ ] Implementar autenticação JWT
