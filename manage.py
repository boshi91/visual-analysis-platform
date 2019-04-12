import os
from config import DATA_DIR, MODEL_DIR, PROJECT_DIR, CACHE_DIR
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import pymysql
pymysql.install_as_MySQLdb()

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

def init():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    if not os.path.exists(MODEL_DIR):
        os.mkdir(MODEL_DIR)
    if not os.path.exists(PROJECT_DIR):
        os.mkdir(PROJECT_DIR)
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)

if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(path)

    init()

    manager.run()
