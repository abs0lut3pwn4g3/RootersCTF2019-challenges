from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = 'notify.login'
login_manager.login_message_category = 'info'