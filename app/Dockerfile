# Use a imagem base do Python
FROM python:3.10-slim-buster

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o diretório de trabalho na imagem
COPY . .

# Exponha a porta em que a aplicação Flask está rodando
EXPOSE 5000

# Comando para executar a aplicação Flask
CMD [ "python", "app.py" ]
