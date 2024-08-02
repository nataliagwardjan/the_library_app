from dotenv import load_dotenv
from pathlib import Path
import os
import pymysql.cursors

base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
load_dotenv(env_file)


def get_db_connection():
    connection = pymysql.connect(
        host=os.environ.get("DATABASE_PORT"),
        user=os.environ.get("MYSQL_USERNAME"),
        password=os.environ.get("MYSQL_USERNAME"),
        database=os.environ.get("DATABASE_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


class Config:
    FLASK_APP = 'library.py'
    PORT = 8080
    DEBUG = True
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    URL_PREFIX = os.environ.get('URL_PREFIX')
    PER_PAGE = 10
