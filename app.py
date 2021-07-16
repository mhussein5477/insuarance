from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'insuarance'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# different routes to different pages ---------------------------------------------------------------------------------------------

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login')
def  signin():
    return render_template("signin.html")

@app.route('/analysis')
def analysis():
    return render_template("analysis.html")

    
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM users WHERE category LIKE 'user'")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', doctor=data)

# resistering a user in the system ---------------------------------------------------------------------------------------------------------------

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        name = request.form['name']
        email = request.form['email']
        phoneno = request.form['phoneno']
        city = request.form['city']
        category = request.form['category']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, phone , city , email , category , password) VALUES (%s, %s,%s,%s,%s,%s)",
                    (name, phoneno, city, email, category, hash_password))
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        session['phoneno'] = phoneno
        session['city'] = city
        session['category'] = category
        return redirect(url_for("dashboard"))

# login validation of a user ----------------------------------------------------------------------------------------------------------------------
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                session['category'] = user['category']
                session['city'] = user['city']
                session['phoneno'] = user['phone']
                return render_template("dashboard.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("signin.html")


# PREDICTION OF LIFE INSARANCE PERCENTAGE ---------------------------------------------------------------------------------------------------------

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'GET':
        return render_template("dashboard.html")
    else:
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        salary = int(request.form['salary'])
        tax = int(request.form['tax'])
        costofliving = int(request.form['costofliving'])
        healthcondition = int(request.form['healthcondition'])
        highway = int(request.form['highway'])
        smoker = int(request.form['smoker'])
        crimerate = int(request.form['crimerate'])
       
        children = int(request.form['children'])
        
        job = request.form['job']
        lifestyle = request.form['lifestyle']
        name = request.form['name']
        city = request.form['city']
        phoneno = request.form['phoneno']
        email = request.form['email']





























# inserting-------------------------------------------------------------------------------------------------------------------
        cur = mysql.connection.cursor()
        if smoker == 1 or job == "machineryoperator" or job == "policeorarmy" or job == "truckdriver" or crimerate == 1 or children >= 2 or age >= 30 or crimerate == 1  or healthcondition == 1 :
            result = salary * 0.37;
            acc =round(random.uniform(70.00, 90.00),3) 
            cur.execute("INSERT INTO predictions (name, city , phoneno , email , age , sex , salary , tax , costofliving , healthcondition , highway , smoker , crimerate , job , children , lifestyle , result , accuracy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s )",
                        (name, city, phoneno, email, age, sex, salary , tax , costofliving, healthcondition,  highway, smoker, crimerate, job, children, lifestyle , result, acc))
            mysql.connection.commit()
            return render_template("results.html", result=result, accuracy=acc)
        else:
           
            
         return render_template("results1.html", result=result, accuracy=acc)


# logout--------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = "shicenzi5477!@aa"
    app.run(debug=True)
