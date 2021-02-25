from flask import render_template, redirect, url_for, session, Blueprint
from form import *
from flask_login import logout_user, login_required
from config import GOOGLE_OAUTH2_CLIENT_ID

bp_auth_app = Blueprint('bp_auth_app', __name__)

@bp_auth_app.route('/register', methods=['GET', 'POST']) # 注册
def register():
    form = FormRegister()

    content = {'form':form, 'google_oauth2_client_id': GOOGLE_OAUTH2_CLIENT_ID}

    return render_template('auth/register.html', **content)

@bp_auth_app.route('/login', methods=['GET', 'POST']) # 登入
def login():
    form = FormLogin()

    content = {'form': form, 'google_oauth2_client_id': GOOGLE_OAUTH2_CLIENT_ID}

    return render_template('auth/login.html', **content)

@bp_auth_app.route('/logout') # 登出
@login_required
def logout():
    session.pop('account', None)     # remove the username from the session if it's there
    logout_user()
    return redirect(url_for('index'))