# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formulario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key = True,  autoincrement = True)

    email = db.Column(db.String(30), nullable = False)
    text = db.Column(db.Text, nullable = False)
     

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python') #Creacion de solicitud de imagen
    button_html = request.form.get('button_html') #determina que el input se esta generando con esta solicitud
    email =  request.form.get('email')
    text =  request.form.get('text')
    with open('form.txt', 'a') as f:
        f.write(f"FORMULARIO\n{email}\n{text}\n")
        
    formulario = Form(email = email,  text = text)
    db.session.add(formulario)
    db.session.commit()

    return render_template('index.html', 
                           button_python=button_python,
                           button_html = button_html,
                           email = email,
                           text = text)


if __name__ == "__main__":
    app.run(debug=True)
