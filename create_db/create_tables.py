import psycopg2

from config import params


def create_tables() -> None:
    tables = [
        '''
        CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(25),
        mobile_phone VARCHAR(25),
        status VARCHAR(25)
        )
        '''
        ,
        '''
        CREATE TABLE courses(course_id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL UNIQUE, code VARCHAR(255) NOT NULL UNIQUE);
        '''
        ,
        '''
        CREATE TABLE user_courses(
        student_id INT NOT NULL,
        course_id INT NOT NULL,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES student(student_id) ON UPDATE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON UPDATE CASCADE
        )
        '''
    ]
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for table in tables:
            cur.execute(table)
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
