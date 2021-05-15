from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        img = request.form['image']
        return render_template("index.html")


if __name__ == '__main__':
    app.run()