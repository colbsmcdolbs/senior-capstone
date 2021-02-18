from flask import Flask, render_template
from helpers.grapher import create_graph
import os

app = Flask(__name__)


@app.route('/')
def index():
    bar = bar_graph()
    return render_template('index.html', plot=bar, heat=)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
