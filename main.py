from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
passwd = '1234'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/restart')
def restart():
    os.system()
    return "Restart Finished"

@app.route('/shutdown')
def shutdown():
    return 'SHUTDOWN'

app.run(host='10')