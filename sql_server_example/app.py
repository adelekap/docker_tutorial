from flask import Flask
import os
import socket

from search_results_sql import insert_data
from utils import get_first_google_result

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/search/<query>")
def search(query):
    first_url = get_first_google_result(query)
    html = f"<h3><a href='{first_url}'>Result</a></h3>"

    return html


@app.route("/search/<query>/store-result")
def store_result(query):
    first_url = get_first_google_result(query)
    insert_data(query, first_url)
    html = f"<h3><a href='{first_url}'>Result</a></h3><b><h2>RESULT INSERTED INTO DB!</h2></b>"
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
