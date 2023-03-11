from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email
from flask import Markup

class NewPropertyForm(FlaskForm):
    title = StringField(Markup('Property Title'), validators=[InputRequired()])
    description = TextAreaField(Markup('Description'), validators=[InputRequired()])
    rooms = StringField(Markup('No. of Rooms'), validators=[InputRequired()])
    bathrooms = StringField(Markup('No. of Bathrooms'), validators=[InputRequired()])
    price = StringField(Markup('Price'), validators=[InputRequired()])
    propertyType = SelectField('Property Type', choices=[('1', 'House'), ('2', 'Apartment')])
    location = StringField(Markup('Location'), validators=[InputRequired()])
    file = FileField('Upload Image Here: ', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only JPEG and PNG images are allowed!')])

