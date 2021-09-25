from flask import Flask, render_template
app = Flask(__name__)

app.debug = True

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('about.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/cadastro')
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