from flask import Flask, render_template,request
app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == "__main__":
	app.run()