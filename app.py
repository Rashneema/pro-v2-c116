from flask import Flask

#Create an object of flask class
app=Flask(__name__)


@app.route("/")
def first_flask():
    return "This is my first flask program"


@app.route("/flask_2")
def second_flask():
    return "python is fun,let's code"

app.run(debug=True)