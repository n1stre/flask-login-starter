from flask_wtf import Form # , RecaptchaField
from wtforms import TextField, PasswordField # BooleanField
from wtforms.validators import Required, Email, EqualTo


# Define the login form (WTForms)

class CommandForm(Form):
  name = TextField('Command name', [
    Required(message='Forgot command name?')
  ])
  type = TextField('Command type', [
    Required(message='Must provide a type. ;-)')
  ])