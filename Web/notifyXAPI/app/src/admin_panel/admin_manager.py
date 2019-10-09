''' Admin Model Views '''

from flask import abort
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from src import admin, db
from src.users.models import User
from src.notifs.models import Notification

class MyAdminModel(ModelView):

    column_exclude_list = ( 'password' )

    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.is_admin:
        	# permission denied
        	abort(403)
        if current_user.is_admin:
            return True
        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is
        not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            #else:
                # login
            #    return redirect(url_for('user.login', next=request.url))


admin.add_view(MyAdminModel(User, session=db.session))
admin.add_view(MyAdminModel(Notification, session=db.session))
