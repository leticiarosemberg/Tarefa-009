from flask import Flask, render_template, request, redirect, flash
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)

app.secret_key = '120302'

app.debug = True

usuarios = [
    {
     'nome': '',
     'email': '',
     'senha': '',
     'endereco': '',
     'checkboxedi': '',
     'checkboxred': '',
     'curriculo': '',
     'radio': ''
     }
]

contact = [
    {'nome': '',
     'email': '',
     'assunto': ''
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('about.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/songs')
def songs_page():
    return render_template('songs.html')

@app.route('/exemplos')
def exemplos_page():
    return render_template('exemplos.html')

@app.route('/projeto')
def projeto_page():
    return render_template('projeto.html')

@app.route('/cadastro')
def cadastro_page():
    return render_template('cadastro.html')

@app.post('/novocadastro')
def cadastrar_page():
    nome_nv = request.form['nome']
    email_nv = request.form['email']
    senha_nv = request.form['senha']
    endereco_nv = request.form['endereco']

    try:
        checkboxedi_nv = request.form['checkboxedi']
    except BadRequestKeyError:
        checkboxedi_nv = None
    try:
        checkboxred_nv = request.form['checkboxred']
    except BadRequestKeyError:
        checkboxred_nv = None
    try:
        curriculo_nv = request.form['curriculo']
    except BadRequestKeyError:
        curriculo_nv = None
    radio_nv = request.form['radio']

    novo_usuario = {
        'nome': nome_nv,
        'email': email_nv,
        'senha': senha_nv,
        'endereco': endereco_nv,
        'checkboxedi': checkboxedi_nv,
        'checkboxred': checkboxred_nv,
        'curriculo': curriculo_nv,
        'radio': radio_nv
        }
    usuarios.append(novo_usuario)

    flash(f'Curriculo de {nome_nv} enviado com sucesso! Entraremos em contato assim que possível :)')

    return redirect('/home')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.post('/novocontact')
def contatar_page():
    nome_nv = request.form['nome']
    email_nv = request.form['email']
    assunto_nv = request.form['assunto']

    novo_contact = {
        'nome': nome_nv,
        'email': email_nv,
        'assunto': assunto_nv
        }
    contact.append(novo_contact)

    flash(f'Olá, {nome_nv} seu recado foi enviado! Responderemos assim que possível :)')

    return redirect('/home')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.post('/entrar')
def entrar_page():
    email_l = request.form['email']
    senha_l = request.form['senha']
    res = None
    for usuario in usuarios:
        if email_l == usuario['email'] and senha_l == usuario['senha']:
            res = True
        else:
            res = False

    if res == True:
        flash('Espero que goste do nosso site :)')
        return redirect('/home')
    else:
        flash('Algo deu errado :(  tente novamente!')
        return redirect('/login')









