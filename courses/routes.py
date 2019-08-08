from flask import Blueprint
from flask import render_template

from utils import get_all_courses

courses = Blueprint('courses', __name__)
title = "Courses page"


@courses.route('/courses')
def all_courses():
    courses_list = get_all_courses()
    return render_template('courses.html', title=title, course_list=courses_list)
