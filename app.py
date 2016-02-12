from flask import Flask, render_template, request, url_for
from forms import loginForm
from controllers.auth.auth import auth
from database.database import db_session

app = Flask(__name__)

app.register_blueprint(auth)

@app.route('/')
def home():
	return "Hello World"

@app.route('/welcome')
def welcome():
	form = loginForm.LoginForm(request.form)
	return render_template("welcome.html", form=form)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
	app.run(debug=True)
