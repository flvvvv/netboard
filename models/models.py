from create_db import db
from datetime import datetime
from flask_login import UserMixin


class Board(db.Model): # board
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"), unique=True)  # foreignkey: auth.id
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    # Setup the relationship
    message = db.relationship("Message", uselist=True, backref="board", cascade="all, delete")  # the one-to-many relationship(board - message)


    def __init__(self, user_id):
        self.user_id = user_id

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()


class Message(db.Model): # msg
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer(), db.ForeignKey('board.id', ondelete="CASCADE")) # foreignkey: board.id
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"))  # foreignkey: auth.id
    message = db.Column(db.Text(64))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, board_id, user_id, message, created_at, update_at):
        self.board_id = board_id
        self.user_id = user_id
        self.message = message
        self.created_at = created_at
        self.updated_at = update_at

    def __repr__(self):
        return '<Message: {}>'.format(self.id)

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, message):
        self.message = message
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()


class User(db.Model, UserMixin): # user
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum('M', 'F'))
    birthday = db.Column(db.DateTime)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    
    board = db.relationship("Board", uselist=False, backref="user", cascade="all, delete",) # (auth - board)
    message = db.relationship("Message", uselist=True, backref="user", cascade="all, delete",)  # (auth - message)


    def __init__(self, email, gender, birthday, username, password):
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User: {}>'.format(self.id)

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()