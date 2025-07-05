# Usa un'immagine base Python slim per ridurre le dimensioni finali
FROM python:3.13-slim

# Imposta variabili d'ambiente per gestire Poetry
ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Aggiorna e installa dipendenze necessarie per build e runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Aggiungi Poetry al PATH
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# Crea e imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto
COPY pyproject.toml ./

# Installa le dipendenze con Poetry
RUN poetry install --no-root

COPY . .

# Espone la porta (se necessaria, altrimenti puoi rimuoverla)
EXPOSE 3000

# Comando di avvio
CMD ["poetry", "run", "python", "index.py"]
