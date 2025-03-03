"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.properties import NewPropertyForm
from .models import Properties


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET', 'POST'])
def properties():
    """Render the new property page"""
    myform = NewPropertyForm()
    
    app.config['UPLOAD_FOLDER'] = "./uploads"
    if request.method == 'POST':
        if myform.validate_on_submit():
            title = myform.title.data
            description = myform.description.data
            rooms = myform.rooms.data
            bathrooms = myform.bathrooms.data
            price = myform.price.data
            propertyType = myform.propertyType.data
            location = myform.location.data
            file = myform.file.data

            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            myform.file.data.save(file_path)

            property = Properties(title,description,rooms,bathrooms,price,propertyType,location, filename)
            db.session.add(property)
            db.session.commit()

            flash('You have successfully added the Property', 'success')
            return redirect(url_for('propertyList'))

        flash_errors(myform)
    return render_template('create.html', form=myform)


@app.route('/properties')
def propertyList():
    "Render a list of properties in the database"
    properties = Properties.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def propertyId(propertyid):    
    "Render a individual property by a specific id"
    property = Properties.query.get_or_404(propertyid)
    return render_template('propertyDetails.html', property=property) 

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
