from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h3>hello<h3>'


@app.route('/post')
def helloworld():
    return 'hello world'




if __name__ == "__main__":
    app.run(debug= True)