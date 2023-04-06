#!/usr/bin/env python3
from flask import Flask, render_template, redirect, request, url_for

from mongoengine import connect

from models import Todo

app = Flask(__name__)
connect('todo_db')


@app.route('/', methods=['GET'])
def homepage():
    tasks = Todo.objects
    return render_template('index.html', tasks=tasks)


@app.route('/', methods=['POST'])
def add_task():
    task = Todo(**request.form)
    task.save()
    return redirect(url_for('homepage'))


@app.route('/delete/<id>', methods=['POST'])
def delete_task(id):
    task = Todo.objects(id=id)
    task.delete()
    return redirect(url_for('homepage'))


@app.route('/update/<id>', methods=['POST'])
def update_task(id):
    task = Todo.objects(id=id).first()
    print(task.to_json())
    if (not task.completed):
        task.update(completed=True)
    else:
        task.update(completed=False)
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
