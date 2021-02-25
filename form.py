from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, SelectField
from wtforms.fields.html5 import EmailField, DateField


class FormRegister(FlaskForm):

    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])

    username = StringField('UserName', validators=[
        validators.DataRequired(),
    ])

    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female') ])

    birthday = DateField('Birthday', format='%m/%d/%Y')

    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])

    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

    submit = SubmitField('Register New Account', render_kw={"onclick": "register()", "type": "button"})

class MessageForm(FlaskForm):
    message = StringField('Message',
                          validators=[validators.DataRequired()])
    submit = SubmitField('Submit',
                         render_kw={'id': 'submit',
                                    'style': 'width:340px',
                                    'type': 'button',
                                    'onclick': 'message_create()'
                                    })

class FormLogin(FlaskForm):
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])

    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
    ])

    remember = BooleanField('remember me')

    submit = SubmitField('Log in',
                         render_kw={'id': 'submit',
                                    'type': 'button',
                                    'onclick': 'login()'
                                    })