from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt

# Configuração do Flask e Banco de Dados
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

# Inicializa extensões
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# Configuração do LoginManager
login_manager.login_view = 'login'
# Session <- conexão ativa 

#
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login e Logout
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        #Login
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso!"})

    return jsonify({"message": "Credenciais inválidas"}), 400


@app.route('/logout', methods=['GET'])
@login_required # Protege a rota para que apenas usuários autenticados possam acessá-la
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})

# Create, Read, Update, Delete (CRUD) de Usuários
@app.route('/user', methods=['POST']) 
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Criação de usuário
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())# Aqui você deve aplicar uma função de hash para segurança
        user = User(username=username, password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário cadastrado com sucesso!"})

    return jsonify({"message": "Dados inválidos!"}), 400

@app.route('/user/<int:user_id>', methods=['GET'])
@login_required
def read_user(user_id):
    user = User.query.get(user_id)
    if user:
        return {"username": user.username}
    return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/user/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.json
    user =User.query.get(user_id)
    
    if user_id != current_user.id and current_user.role != 'admin':
        # Verifica se o usuário está tentando atualizar outro usuário sem ser admin
        return jsonify({"message": "Atualização não permitida"}), 403
    
    if user and data.get('password'):
        user.password = data.get('password')
        db.session.commit()

        return jsonify({"message": f"Usuário {user_id} atualizado com sucesso!"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)

    if current_user.role != 'admin':
        # Verifica se o usuário é admin para permitir a deleção
        return jsonify({"message": "Apenas administradores podem deletar usuários"}), 403

    if user_id == current_user.id:
        return jsonify({"message": "Deleção não permitida"}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {user_id} deletado com sucesso!"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404

# Rota de teste
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'

# Debug mode
if __name__ == '__main__':
    app.run(debug=True)