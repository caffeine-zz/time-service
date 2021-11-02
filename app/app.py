from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return '{} {}'.format(str("Server local time:"), current_time)

if __name__ == "__main__":
    app.run()
