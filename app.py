from create_db import db 
import config
from view.utils import query_objects_pagination

from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from models.user.models import User

from view.auth import bp_auth_app
from view.message import bp_message_app

from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

from flask_restful import Api


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
bootstrap = Bootstrap(app)
csrf_protect = CSRFProtect(app)

# login manager
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# ============= #

# API
auth_api = Api(bp_auth_api, decorators=[csrf_protect.exempt])
auth_api.add_resource(ApiLogin, '/login')
auth_api.add_resource(ApiRegister, '/register')

message_api = Api(bp_message_api, decorators=[csrf_protect.exempt])
message_api.add_resource(ApiMessage, '')

auth_google_api = Api(bp_google_auth, decorators=[csrf_protect.exempt])
auth_google_api.add_resource(GoogleAuthApi, '')
# ============= #

#  blueprint
app.register_blueprint(bp_auth_app, url_prefix='/auth')
app.register_blueprint(bp_message_app, url_prefix='/message')

app.register_blueprint(bp_auth_api, url_prefix='/api/auth')
app.register_blueprint(bp_message_api, url_prefix='/api/message')

app.register_blueprint(bp_google_auth, url_prefix='/api/google/auth')
# ============= #

# the toolbar is only enabled in debug mode:
app.debug = False
toolbar = DebugToolbarExtension(app)
logger = app.logger

@app.route('/')
def index():
    users = User.query.filter(User.id != 0)
    pagination= query_objects_pagination(query_objects=users, per_page=8) # 分页
    content = {'title': '首页', 'users': users, 'pagination_users':pagination['pagination_items'], 'pagination': pagination['pagination']}
    return render_template('index.html', **content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=200)
