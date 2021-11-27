from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///descarte.sqlite3'
db = SQLAlchemy(app)


class Descarte(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(100), nullable=False)
    ecoponto = db.Column(db.String(150), nullable=False)
    item = db.Column(db.String(150), nullable=False)
    quantidade = db.Column(db.Integer)

    def __init__(self, nome, endereco, numero, bairro, ecoponto, item, quantidade):
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.ecoponto = ecoponto
        self.item = item
        self.quantidade = quantidade

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    descartes = Descarte.query.all()
    return render_template('lista.html', descartes=descartes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descarte = Descarte(request.form['nome'], request.form['endereco'], request.form['numero'], request.form['bairro'], request.form['ecoponto'], request.form['item'], request.form['quantidade'])
        db.session.add(descarte)
        db.session.commit()
        return redirect(url_for('cadastrar'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    descarte = Descarte.query.get(id)
    if request.method == 'POST':
        descarte.nome = request.form['nome']
        descarte.localidade = request.form['endereco']
        descarte.localidade = request.form['numero']
        descarte.localidade = request.form['bairro']
        descarte.localidade = request.form['ecoponto']
        descarte.item = request.form['item']
        descarte.quantidade = request.form['quantidade']
        db.session.commit()
        return redirect(url_for('cadastrar'))
    return render_template('edit.html', descarte=descarte)


@app.route('/delete/<int:id>')
def delete(id):
    descarte = Descarte.query.get(id)
    db.session.delete(descarte)
    db.session.commit()
    return redirect(url_for('cadastrar'))


@app.route('/contato')
def contatar():
    return render_template('contato.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
