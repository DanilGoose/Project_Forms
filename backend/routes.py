from flask import render_template, redirect, url_for, request

from backend import app, db
from .models import Message


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', title='Главная')


@app.route('/account', methods=['GET'])
def account():
    return render_template('account.html', title='Аккаунт')


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html', messages=Message.query.all(), title='Эксперименты')


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']

    db.session.add(Message(text))
    db.session.commit()

    return redirect(url_for('test'))
