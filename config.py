# CWBS configuration file
# db config
MYSQL_IP = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_DB = 'x3_development'
SQLALCHEMY_DATABASE_URI = 'mysql://' + MYSQL_USER + ':' + MYSQL_PASS + '@' \
                          + MYSQL_IP + '/' + MYSQL_DB
# 'sqlite:///cidashboard.db'   # Use SQLite for developing mode only
SQLALCHEMY_TRACK_MODIFICATIONS = False

# debugging
DEBUG = False
FLASK_DEBUG = 0

# host IP port
APP_HOST = 'localhost'
APP_PORT = 3030

# key for token
SECRET_KEY = '3d1515ab-c760-4282-953a-31211aa7e2c5'
