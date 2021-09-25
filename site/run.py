from flask import Flask, render_template, request
app = Flask(__name__)

usuarios = [
    {'nome': 'angela', 'email': 'anjoca@gmail.com', 'senha': 1234},
    {'nome': 'cristina', 'email': 'cricri@gmail.com', 'senha': 4321},
]

app.debug = True

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('about.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.get('/cadastro')
def cadastro_page():
    return render_template('cadastro.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/songs')
def songs_page():
    return render_template('songs.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/exemplos')
def exemplos_page():
    return render_template('exemplos.html')

@app.route('/projeto')
def projeto_page():
    return render_template('projeto.html')

@app.post('/addcadastro')
def cadastrar_page():
    nome_novo = request.form['nome']
    email_novo = request.form['email']
    senha_novo = request.form['senha']

    novo_usuario = {
    'nome': nome_novo,
    'email': email_novo,
    'senha': senha_novo
    }
    usuarios.append(novo_usuario)
    return 'Usuário Cadastrado'