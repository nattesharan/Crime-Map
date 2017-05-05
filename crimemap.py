from flask import Flask,request,render_template,url_for,redirect
from dbhelper import DBHelper
app = Flask(__name__)
DB = DBHelper()
@app.route('/')
def home():
    try:
        data = DB.get_all_crimes()
        print(data)
    except Exception as E:
        print(E)
        data = None
    return render_template('home.html')
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
    date = request.form['date']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    description = request.form['description']
    DB.add_crime(category, date, latitude, longitude, description)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(port=int('3000'),debug = True)