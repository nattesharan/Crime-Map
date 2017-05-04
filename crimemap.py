from flask import Flask,request,render_template
from dbhelper import DBHelper
app = Flask(__name__)
DB = DBHelper()
@app.route('/')
def home():
    return '<html><body><h1><strong><i>Hello, this is home</i></strong></h1></body></html>'
if __name__ == '__main__':
    app.run(port=int('3000'),debug = True)