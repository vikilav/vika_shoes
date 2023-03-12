from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    template = 'main.html'
    return render_template(template)
