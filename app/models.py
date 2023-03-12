from . import db

class Properties(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(500))
    rooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    propertyType = db.Column(db.String(80))
    location = db.Column(db.String(80))
    image_filename = db.Column(db.String(255))

    def __init__(self, title, description, rooms, bathrooms, price, propertyType, location, image_filename):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.propertyType = propertyType
        self.location = location
        self.image_filename = image_filename

    def __repr__(self):
        return '<Title %r>' % self.title
