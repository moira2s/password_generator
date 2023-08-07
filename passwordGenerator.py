import random
from flask import Flask
app = Flask(__name__)

@app.route("/")

def passwordGenerator():
    specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    letters = "ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    passwordLength = 20
    password = ''.join(random.choices(specialChars + letters + digits, k=passwordLength))

    return "You password is: " + password


if __name__ == '__main__':
    app.run(debug=True, port=5001)
