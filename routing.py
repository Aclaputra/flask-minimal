from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello/<name>')
def helloName(name):
    return '<h1>Hello, %s!</h1>' % name