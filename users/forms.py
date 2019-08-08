import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length


class NewUserForm(FlaskForm):
    name = StringField("*Name", validators=[DataRequired(), Length(2)])
    email = StringField("*E-mail", validators=[DataRequired(), Email()])
    phone = StringField("Phone")
    mobile_phone = StringField("Mobile phone")
    status = SelectField("Status", choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive')
    submit = SubmitField('Create')

    def validate_mobile_phone(self, mobile_phone):
        pattern = re.compile('^[+]*[1-9]{1,3}[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$')
        if not pattern.match(mobile_phone.data):
            raise ValidationError("Phone should be in international format")


class UpdateUserForm(FlaskForm):
    name = StringField("*Name", validators=[DataRequired(), Length(2)])
    email = StringField("*E-mail", validators=[DataRequired(), Email()])
    phone = StringField("Phone")
    mobile_phone = StringField("Mobile phone")
    status = SelectField("Status", choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive')
    courses = SelectField('Courses', choices=[])
    submit = SubmitField('Save')

    def validate_mobile_phone(self, mobile_phone):
        pattern = re.compile('^[+]*[1-9]{1,3}[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$')
        if not pattern.match(mobile_phone.data):
            raise ValidationError("Phone should be in international format")

# This part doesn't ready
class SearchAndSortForm(FlaskForm):
    search = StringField('')
    per_page_choises = [(10, 10), (15, 15), (20, 20)]
    select = SelectField(choices=per_page_choises)
