from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.')

# Rota Principal (Futurista)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para Mulheres (Botão SOS com Logo e Sirene)
@app.route('/panic')
def panic():
    return render_template('panic.html')

# NOVO: Painel de Cadastro das Pessoas de Confiança
@app.route('/register')
def register():
    return render_template('register.html')

# Rota para Pessoas de Confiança (Visualização de Alertas)
@app.route('/trusted')
def trusted():
    return render_template('trusted.html')

# Rota para Administração
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Rota para servir arquivos estáticos (Imagens e Áudio)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)