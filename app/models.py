from main import db, app, migrate
from datetime import datetime


class Music(db.Model):
    __tablename__ = 'musics'

    id = db.Column(db.Integer, primary_key=True)
    musicName = db.Column(db.String, nullable=False)
    artist = db.Column(db.String,)
    album = db.Column(db.String,)
    genre = db.Column(db.String,)
    evaluation = db.Column(db.Integer,)
    comment = db.Column(db.String,)
    time = db.Column(db.String,)
    bitRate = db.Column(db.String,)
    fileType = db.Column(db.String, nullable=False)
    fileSize = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    url = db.Column(db.String,)
    createdAt = db.Column(db.String, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.String, nullable=False,
                          default=datetime.now, onupdate=datetime.now)
    music_photos = db.relationship(
        'Music_Photo', backref='music', uselist=True, cascade='all, delete',)


class Music_Photo(db.Model):
    __tablename__ = 'music_photos'
    
    id = db.Column(db.Integer, primary_key=True)
    musicId = db.Column(db.Integer, db.ForeignKey('musics.id'))
    fileName = db.Column(db.String)
    fileType = db.Column(db.String, nullable=False)
    fileSize = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.String, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.String, nullable=False,
                          default=datetime.now, onupdate=datetime.now)
    

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    artistName = db.Column(db.String)
    createdAt = db.Column(db.String, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.String, nullable=False,
                          default=datetime.now, onupdate=datetime.now)


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genreName = db.Column(db.String)
    createdAt = db.Column(db.String, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.String, nullable=False,
                          default=datetime.now, onupdate=datetime.now)
