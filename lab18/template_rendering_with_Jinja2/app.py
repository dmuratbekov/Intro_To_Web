from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Maksat', 'Bakai', 'Aruuke']

    return render_template('index.html', names=names, title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)