from flask import Flask
from flask import render_template



app = Flask(__name__,template_folder='templates')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/post')
def helloworld():
    return 'hello world'




if __name__ == "__main__":
    app.run(debug= True)