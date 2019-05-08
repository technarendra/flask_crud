from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = '23453451235'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudapplication'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    cur.close()




    return render_template('Index.html', students=data )



# @app.route('/')
# def Index():
# 	return render_template("Index.html")


@app.route('/insert', methods=['POST'])
def insert():

	if request.method == "POST":
		flash("Data Inserted Successfully")
		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO students(name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
		mysql.connection.commit() 
		return redirect(url_for('Index'))



if __name__=="__main__":
	app.run(debug=True)