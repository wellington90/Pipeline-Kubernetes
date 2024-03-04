
CREATE USER 'app'@'%' IDENTIFIED BY 'Senha123';
GRANT ALL PRIVILEGES ON meubanco.* TO 'app'@'%';
FLUSH PRIVILEGES;

USE meubanco;

CREATE TABLE mensagens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    mensagem TEXT NOT NULL
);
