import psycopg2

from config import params


def add_user(name, email, phone, mobile_phone, status) -> None:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO student (name, email, phone, mobile_phone, status) VALUES (%s, %s, %s, %s, %s);",
                    (name, email, phone, mobile_phone, status,))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def get_all_users() -> []:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM student;")
        users_list = cur.fetchall()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return users_list


def get_filtered_by_id_users(value) -> []:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE student_id = %s;", (value,))
        users_list = cur.fetchall()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return users_list


def get_filtered_by_name_users(value) -> []:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE name = %s;", (value,))
        users_list = cur.fetchall()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return users_list


def get_all_courses() -> []:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM courses;")
        courses_list = cur.fetchall()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return courses_list


def get_users(offset=0, per_page=10) -> []:
    users_list = get_all_users()
    return users_list[offset: offset + per_page]


def delete_user_by_id(user_id):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM student WHERE student_id = %s;", (user_id,))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
