from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required

mod_home = Blueprint('home', __name__)

@mod_home.route('/')
def homepage():
    return render_template('home/index.html', title="Welcome")

@mod_home.route(
  '/users/<user_id>/books/<book_id>', 
  methods=['GET', 'POST']
)
def users_books(user_id, book_id):
  if request.method == 'GET':
      return jsonify({
        'user': user_id,
        'title': request.args.get('title'),
        'description': request.args.get('description'),
      })
  else:
    return jsonify({
      'user': user_id,
      'book': book_id,
    })

@mod_home.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")