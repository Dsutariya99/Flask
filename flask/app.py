from flask import Flask, render_template
# print(Flask.__version__)

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/welcome/<name>")
def welcome(name):
    return '<h1>welcome user'+name + '!</h1>'

if __name__ == "__main__":
    app.run(debug=True)