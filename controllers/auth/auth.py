from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def signup():
	# form = loginForm.LoginForm(request.form)
	# if request.method == 'POST' and form.validate():
	# 	return "Thank you " + request.form['email'] + " for signing up on Scholytics. "
	# else:
	return "Successful Testing of modularization"
