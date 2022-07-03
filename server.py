from flask import Flask


app = Flask('server')


@app.get("/")
def home():
    return "Hello from flask server"


@app.get("/test")
def test():
    return "This is just a simple test"


app.run(debug=True)
