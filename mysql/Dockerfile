# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Copie o script SQL para inicializar o banco de dados
COPY sql.sql /docker-entrypoint-initdb.d/

# Defina o diretório de trabalho
WORKDIR /var/lib/mysql/

# Exponha a porta MySQL
EXPOSE 3306
