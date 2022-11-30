from flask import Flask, render_template, url_for,request,redirect
from flask_mysqldb import MySQL
import functions as function

app = Flask('__name__')
mysql = MySQL(app)
SECRET_KEY = 'desafio4'

app.config['MYSQL_Host']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='contato'



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def home1():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/contato', methods=['POST','GET'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto,descricao)VALUES (%s,%s,%s)",(email,assunto,descricao))
        mysql.connection.commit()

        cur.close()
        
        return redirect('/contato')
        
    return render_template('contato.html')

@app.route('/users')
def users():
    userDetails = function.findUsers()
   

    return render_template("users.html", userDetails=userDetails)


if __name__ == '__main__':
  app.run(debug=True)

