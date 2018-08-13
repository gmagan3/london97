from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, Flask!'
@app.route("/david")
def david():
    return "Hello, David!"
@app.route("/maria")
def maria():
    return "Hello, Maria!"
