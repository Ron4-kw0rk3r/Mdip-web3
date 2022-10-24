# scr code in flask web site market digital inovation profesionality


from crypt import methods
from flask import Flask , request , render_template
from flask import url_for , redirect
import time
from flask_pymongo import PyMongo
from requests import session




app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://kwork:Password01@cluster0.dy9g7dk.mongodb.net/workdb?retryWrites=true&w=majority'


mongoup = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def inhome():
    return render_template('index.html')





@app.route('/get-login', methods=["GET","POST"])

def login():
    #session.clear()
    if request.method == "POST":
        return render_template("/get-login.html")


# header --> clubster  intaeguers

@app.route('/searching', methods=['GET', 'POST'])

def searching():
    if request.method == 'POST':
        if request.form['submit_button'] == 'search':
            return render_template('searching.html')
        else :
            return render_template('error_crashed.html')
@app.route('/service', methods=["POST"])
def service():
    if request.method == "POST":
        if request.form['submit_button1'] == 'services':
            return render_template('services.html')
        else :
            return render_template('error_crashed.html')
@app.route('/contact' , methods=["POST"])
def contact():
    if request.method == "POST":
        if request.form['submit_button2'] == 'contact':
            return render_template('services.html')
        else :
            return render_template('error_crashed.html')
@app.route('/shop', methods=["POST"])
def shop():
    if request.method == "POST":
        if request.form['submit_button3'] == 'shop':
            return render_template('market.html')
        else :
            return render_template('error_crashed.html')

@app.route('/about', methods=["POST"])
def about():
    if request.method == "POST":
        if request.form['submit_button4'] ==  'about':
            return render_template('about.html')
        else :
            return render_template('error_crashed.html')



@app.route('/finder', methods=["GET , POST"])
def finder():
    if request.method == "GET":
        pass
        print("focus_versionFinderv0.0.1")
    else:
        print("focus_versionFinderv0.0.1")



if __name__ == "__main__":
    
    app.run(debug=True, port=5050)
