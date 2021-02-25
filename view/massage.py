from flask import Blueprint

from models.message.models import Message
from models.board.models import Board
from models.user.models import User

from form import MessageForm
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from view.utils import query_objects_pagination
from datetime import datetime

bp_message_app = Blueprint('bp_message_app', __name__)

@bp_message_app.route('/<userid>', methods=['GET'])
def message(userid):
    board = Board.query.filter(Board.user_id == userid).first()
    form = MessageForm()
    messages = Message.query.filter_by(board_id = board.id).order_by(Message.updated_at.desc())
    pagination= query_objects_pagination(query_objects=messages, per_page=4) # 分页

    content = {'form': form, 'messages': messages, 'board': board,
               'pagination': pagination['pagination'], 'pagination_items': pagination['pagination_items']}

    return render_template('message/message.html', **content)