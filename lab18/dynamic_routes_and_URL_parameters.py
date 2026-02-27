from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'<h2>Hello, {escape(name.capitalize())}!</h2>'

if __name__ == '__main__':
    app.run(debug=True)