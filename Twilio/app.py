from flask import Flask
from xml.dom.minidom import parse

app = Flask(__name__)


@app.route("/")
def hello():
    DOMTree = parse("response.xml")
    data = DOMTree.documentElement
    message = data.getElementsByTagName('Body')[0]
    return message.childNodes[0].data


if __name__ == "__main__":
    app.run()
