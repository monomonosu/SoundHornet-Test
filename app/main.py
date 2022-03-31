from flask import Flask, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from models import *

app = Flask(__name__)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
ma = Marshmallow(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test-page")
def testPage():
    return render_template('test.html')


@app.route("/test", methods=['GET'])
def getTest():
    musics = Music.query.all()
    return jsonify(MusicSchema(many=True).dump(musics))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
