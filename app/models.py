from main import db,app,migrate

# テスト
class User(db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
        