import random
#from flask import Flask
#app = Flask(__name__)

#@app.route("/")

def passwordGenerator():
    specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    letters = "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    passwordLength = 20
    password = ''.join(random.choices(specialChars + letters + digits, k=passwordLength))

    print("Your password is: " + password)

passwordGenerator()
