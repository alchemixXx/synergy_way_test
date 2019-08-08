import psycopg2
from psycopg2.extensions import AsIs

from config import params, Config


def grant_privileges() -> None:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DROP USER IF EXISTS %s", (AsIs(Config.PG_USER),))
        cur.execute("CREATE USER %s with ENCRYPTED PASSWORD %s;", (AsIs(Config.PG_USER), Config.PG_PASSWORD,))
        cur.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s;", (AsIs(Config.DB_NAME), AsIs(Config.PG_USER),))
        cur.execute("ALTER USER %s WITH SUPERUSER;", (AsIs(Config.PG_USER),))
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
