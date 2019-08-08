import psycopg2

from config import params

courses_dict = {'Python-Base': 'P0123456',
                'Python-Database': 'P234567',
                'HTML': 'H345678',
                'Java-Base': 'J456789',
                'JavaScript-Base': 'JS543210'}

users_list = [
    ['Pa P', 'test@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['P Pa', 'test2@gmail.com', '', '+38(096)-89-29-791', 'Inactive'],
    ['Ps P', 'test3@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['P Ps', 'test4@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Pra Pr', 'test5@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Pr Pra', 'test6@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Pra Pra', 'test7@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Prb Pr', 'test8@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Pr Prb', 'test9@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Prb Prb', 'test10@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Prv Pr', 'test11@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
    ['Pr Prv', 'test12@gmail.com', '937-99-92', '+38(096)-89-29-791', 'Active'],
]


def fill_tables() -> None:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for users in users_list:
            cur.execute("INSERT INTO student (name, email, phone, mobile_phone, status) VALUES (%s, %s, %s, %s, %s);",
                        (users[0], users[1], users[2], users[3], users[4],))

        for course_name, course_code in courses_dict.items():
            cur.execute("INSERT INTO courses (name, code) VALUES (%s, %s);",
                        (course_name, course_code,))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
