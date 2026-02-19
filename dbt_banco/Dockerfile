# Arquivo: dbt_banco/Dockerfile
FROM python:3.11-slim

# Atualiza o SO e instala o essencial para o driver do Postgres (psycopg2) compilar
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instala o dbt e trava o protobuf para não dar pau no MessageToJson
RUN pip install --no-cache-dir dbt-postgres==1.7.9 "protobuf<5.0.0"

# Define a pasta de trabalho dentro do container
WORKDIR /usr/app/dbt_project

# Comando para manter o container vivo
CMD ["tail", "-f", "/dev/null"]