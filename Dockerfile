FROM python:3.11-slim

# Instala as dependências do sistema necessárias para compilar mysqlclient
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libmariadb-dev \
       pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos
COPY requirements.txt /app/

# Instala os requisitos do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . /app/

# Comando padrão para rodar o Django
# Executa as migrações do Django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
