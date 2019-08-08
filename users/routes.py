from flask import Blueprint, request
from flask import render_template, flash, redirect, url_for
from flask_paginate import Pagination, get_page_args

from forms import NewUserForm, UpdateUserForm, SearchAndSortForm
from utils import get_all_courses, get_filtered_by_id_users, get_all_users, get_users, add_user, delete_user_by_id, \
    get_filtered_by_name_users

users = Blueprint('users', __name__)

title = "Users page"


@users.route('/', methods=['GET', 'POST'])
@users.route('/users', methods=['GET', 'POST'])
def all_users():
    # if request.method == "POST":
        # if search == "none":
    users_list = get_all_users()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(users_list)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('users.html',
                           title=title,
                           user_list=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           change_offset=get_users,
                           )

    # Something about search realization

    # else:
    #     users_list = get_filtered_by_name_users(search)
    #     page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    #     total = len(users_list)
    #     pagination_users = users_list
    #     pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    #     return render_template('users.html',
    #                            title=title,
    #                            user_list=pagination_users,
    #                            page=page,
    #                            per_page=per_page,
    #                            pagination=pagination,
    #                            change_offset=get_users,
    #                            form=search
    #                            )


# This part doesn't finished

# @users.route('/results')
# def search_results(form):
#     results = []
#     search_string = form.search.data
#
#     if search_string == '':
#         results = get_filtered_by_name_users(search_string)
#
#     if not results:
#         return redirect('/')
#     else:
#         return render_template('users.html', title=title, user_list=results)



@users.route('/add_user', methods=['GET', 'POST'])
def add_new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        name = form.name.data,
        email = form.email.data,
        phone = form.phone.data,
        mobile_phone = form.mobile_phone.data,
        status = form.status.data
        add_user(name, email, phone, mobile_phone, status)
        flash('User created successfully', 'success')
        return redirect(url_for('users.all_users'))
    return render_template('add_user.html', form=form, title=title)


@users.route('/change_user/<int:user_id>', methods=['GET', 'POST'])
def change_user(user_id):
    changed_user = get_filtered_by_id_users(user_id)[0]
    changed_name = changed_user[1]
    form = UpdateUserForm()
    if form.validate_on_submit():
        changed_user.name = changed_name
        changed_user.email = form.email.data
        changed_user.phone = form.phone.data
        changed_user.mobile_phone = form.mobile_phone.data
        changed_user.status = form.status.data
        flash('User updated successfully', 'success')
    elif request.method == "GET":
        form.name.data = changed_user[1]
        form.email.data = changed_user[2]
        form.phone.data = changed_user[3]
        form.mobile_phone.data = changed_user[4]
        form.status.data = changed_user[5]
        form.courses.choices = [(course[0], course[1]) for course in get_all_courses()]
    return render_template('chage_user.html', form=form, title=title)


@users.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    delete_user_by_id(user_id)
    return redirect(url_for('users.all_users'))
