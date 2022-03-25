from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db=SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)