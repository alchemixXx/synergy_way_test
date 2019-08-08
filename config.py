# MySQL
# MYSQL_DATABASE_HOST = '127.0.0.1'
# MYSQL_DATABASE_PORT = '3306'
# MYSQL_DATABASE_USER = 'synergy'
# MYSQL_DATABASE_PASSWORD = 'root'
# MYSQL_DATABASE_DB = 'users'
# MYSQL_DATABASE_CHARSET = 'utf-8'
#


# PostgreSQL
class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "synergy"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "users"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFUALT_DB_NAME = 'postgres'


params = {
    "dbname": Config.DB_NAME,
    "user": Config.PG_USER,
    "host": Config.PG_HOST,
    "password": Config.PG_PASSWORD
}
