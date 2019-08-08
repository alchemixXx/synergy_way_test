from config import Config
from courses.routes import courses
from courses_app import app
from users.routes import users


def run_app():
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(courses)
    return app


if __name__ == '__main__':
    run_app().run(debug=True)
