import os

from dotenv import load_dotenv

# Loading environments variables. Override in prod.
load_dotenv()

# Setting logging
LOG_CONFIG = "logging.ini"

# Mysql config
SQLALCHEMY_MYSQL_URI = (
    "mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=os.getenv("MYSQL_PORT"),
        db_name=os.getenv("MYSQL_DATABASE"),
    )
)