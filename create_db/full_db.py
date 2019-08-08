from create_tables import create_tables
from create_user import grant_privileges
from fill_tables import fill_tables
from init_db import init_db

if __name__ == '__main__':
    init_db()
    grant_privileges()
    create_tables()
    fill_tables()
