# syntax=docker/dockerfile:1

FROM python:3.13-slim AS base

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.5

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

# Copia configs do Poetry
COPY pyproject.toml poetry.lock* ./

# Instala dependências
RUN poetry install --without dev --no-interaction --no-ansi

# Copia o código
COPY . .

# Expor porta
EXPOSE 8000

# Comando default
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
