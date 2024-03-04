from flask import Flask, request, jsonify, render_template
from flaskext.mysql import MySQL
import random
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def formulario():
    return render_template('form.html')

@app.route('/adicionar_mensagem', methods=['POST'])
def adicionar_mensagem():
    try:
        nome = request.form["nome"]
        mensagem = request.form["mensagem"]

        # Gerar um ID aleatório
        id = random.randint(1, 999)

        # Criar uma conexão com o banco de dados
        cursor = mysql.get_db().cursor()

        # Inserir dados no banco de dados
        cursor.execute("INSERT INTO mensagens (id, nome, mensagem) VALUES (%s, %s, %s)", (id, nome, mensagem))
        mysql.get_db().commit()
        cursor.close()

        return jsonify({"message": "New record created successfully"}), 200
    except KeyError as e:
        return jsonify({"error": "Missing field: {}".format(str(e))}), 400
    except Exception as e:
        return jsonify({"error": "Database error: {}".format(str(e))}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
