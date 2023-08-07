import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/generate',methods=['POST','GET'])
def passwordGenerator():
    specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    letters = "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    passwordLength = 20
    password = ''.join(random.choices(specialChars + letters + digits, k=passwordLength))
    return render_template("index.html",password=password)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
