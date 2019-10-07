import os
import urllib.parse as up

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import url_for, render_template, send_from_directory, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src import api, db, ma, create_app, Config, bp, bcrypt, jwt, admin, login_manager


# config = configs.get(config)
config = Config

extensions = [api, db, ma, admin, jwt, bcrypt, login_manager]
bps = [bp]

app = create_app(__name__, config, extensions=extensions, blueprints=bps)
app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=2)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def _shell_context():
    return dict(
        app=app,
        db=db,
        ma=ma,
        config=config
        )


@manager.command
def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = up.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.option('-A', '--application', dest='application', default='', required=True)
@manager.option('-n', '--name', dest='name')
@manager.option('-l', '--debug', dest='debug')
@manager.option('-f', '--logfile', dest='logfile')
@manager.option('-P', '--pool', dest='pool')
@manager.option('-Q', '--queue', dest='queue')
@manager.option('-c', '--concurrency', dest='concurrency', default=2)
def worker(application, concurrency, pool, debug, logfile, name, queue):
    celery.start()


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    manager.run()
