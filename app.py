from flask import Flask
import os
import socket

app = Flask(__name__)
c = 0

@app.route("/")
def current_value_c():
    return f"Current counter value: {c}"

@app.route("/stat")
def increment_с():
    global c
    msg = f"Current counter value: {c}"
    c += 1
    return msg + f"\nThe counter value has been incremented."

@app.route("/about")
def hello():
    
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
