# =========================
# Build dev
# =========================
FROM python:3.13-alpine AS builder

# Variabili ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

# Dipendenze build
RUN apk add --no-cache curl build-base libffi-dev openssl-dev musl-dev git

WORKDIR /app

# Installa Poetry via script ufficiale
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copia solo i file di dipendenze
COPY pyproject.toml poetry.lock* ./

# Installa le dipendenze globalmente senza dev
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# Copia il codice
COPY . .

RUN rm -f pyproject.toml poetry.lock*

# =========================
# Runtime
# =========================
FROM python:3.13-alpine AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Dipendenze runtime
RUN apk add --no-cache libffi openssl

WORKDIR /app

# Copia solo site-packages e codice (nessun Poetry)
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /app /app

# Comando di default
CMD ["python", "index.py"]
