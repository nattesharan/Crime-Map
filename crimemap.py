from flask import Flask,request,render_template,url_for,redirect
from dbhelper import DBHelper
app = Flask(__name__)
DB = DBHelper()
@app.route('/')
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as E:
        print(E)
        data = None
    return render_template('home.html',data = data)
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
if __name__ == '__main__':
    app.run(port=int('3000'),debug = True)