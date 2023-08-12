from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forms.db'
db = SQLAlchemy(app)

arr = [1, 2, 3, 101]

@app.route("/")
def main():
    return render_template('index.html', arr=arr, title='Главная')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)