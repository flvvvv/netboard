from flask import Blueprint, jsonify
from models.message.models import Message
from models.board.models import Board
from models.user.models import User


bp_ma_app = Blueprint('bp_ma_app', __name__)

@bp_ma_app.route('/auth', methods=['GET', 'POST'])
def user_schema():
    users = User.query.all()
    output = user_schema.dump(users)
    return jsonify({'auth': output})

@bp_ma_app.route('/createuser', methods=['GET', 'POST'])
def create_user():
    input_data = {}
    input_data['account'] = 5
    input_data['username'] = '5'
    input_data['password'] = '5'