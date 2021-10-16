from flask import Flask
import os
import socket

app = Flask(__name__)
counter = 0

@app.route("/")
def current_value_counter():
    return f"Current counter value: {counter}"

@app.route("/stat")
def increment_counter():
    global counter
    message = f"Current counter value: {counter}"
    counter += 1
    return message + f"\nThe counter value has been incremented."

@app.route("/about")
def hello():
    
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
