from werkzeug import check_password_hash, generate_password_hash
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

from app import db
from app.mod_commands.forms import CommandForm
from app.mod_commands.models import Command

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_commands = Blueprint('commands', __name__)

# Set the route and accepted methods
@mod_commands.route('/new', methods=['GET', 'POST'])
def create():

  # If sign in form is submitted
  form = CommandForm(request.form)

  # Verify the sign in form
  # if form.validate_on_submit():

  return render_template("commands/create.html", form=form)