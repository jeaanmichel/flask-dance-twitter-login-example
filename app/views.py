from app import app, twitter_blueprint
from models import User, OAuth, db
from flask import url_for, redirect, flash, render_template
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Definir sqlalchemy backend
twitter_blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user, user_required = False)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@oauth_authorized.connect_via(twitter_blueprint)
def twitter_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", category="error")
        return False

    account_info = blueprint.session.get('account/verify_credentials.json')

    if account_info.ok:
        account_info_json = account_info.json()
        user_id = str(account_info_json['id'])
        username = account_info_json['screen_name']

        query = OAuth.query.filter_by(
            provider=blueprint.name,
            provider_user_id=user_id,
        )
        try:
            oauth = query.one()
        except NoResultFound:
            oauth = OAuth(
                provider=blueprint.name,
                provider_user_id=user_id,
                token=token,
            )

        if oauth.user:
            login_user(oauth.user)
            flash("Successfully signed in with Twitter.")

        else:
            user = User(username=username)
            oauth.user = user
            db.session.add_all([user, oauth])
            db.session.commit()
            login_user(user)
            flash("Successfully signed with Twitter.")

    else:
        msg = "Failed to fetch user info from GitHub."
        flash(msg, category="error")
        return False


login_manager.init_app(app)
