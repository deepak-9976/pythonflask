from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)


@app.route('/')
def helloworld():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
