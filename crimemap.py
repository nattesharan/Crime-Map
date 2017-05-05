from flask import Flask,request,render_template,url_for,redirect
from dbhelper import DBHelper
import json
app = Flask(__name__)
DB = DBHelper()
categories = ['mugging', 'break-in']
@app.route('/')
def home():
    try:
        data = DB.get_all_crimes()
        data = json.dumps(data)
    except Exception as E:
        print(E)
        data = None
    return render_template('home.html',data = data,categories = categories)
@app.route('/add', methods = ['POST'])
def add():
    try:
        data = request.form['userinput']
        DB.add_input(data)
    except Exception as E:
        print(E)
    return redirect(url_for('home'))
@app.route('/clear')
def clear():
    try:
        DB.clear_all()
    except Exception as E:
        print(E)
    return redirect(url_for('home'))
@app.route('/submitcrime',methods = ['POST'])
def submitcrime():
    category = request.form['category']
    if category not in categories:
        return home()
    date = request.form['date']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    description = request.form['description']
    DB.add_crime(category, date, latitude, longitude, description)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(port=int('3000'),debug = True)