"""Models for restaurant ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tabalename__ = "user_r"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="user")
    rests = db.relationship("Restaurant", secondary="fav_rest", back_populates="users")

    def __repr__(self):
        "Show user_id and user_name"

        return f"<user_id: {self.user_id} user_name: {self.fname} {self.lname}>"

class fav_rest(db.Model):
    """User's favorite restaurant -- associate table"""

    __tablename__ = "fav_rest"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.restaurant_id"), nullable=False)

    
class Restaurant(db.Model):
    """A restaurent"""

    __tablename__ = "restaurant"

    restaurant_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    yelp_id = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String)
    url = db.Column(db.String)

    # ratings = db.relationship("Rating", back_populates="restaurant")
    users = db.relationship("User", secondary="fav_rest", back_populates="rests")

    def __repr__(self):
        """Show restaurant id and name"""

        return f"<rest_id: {self.restaurant_id} rest_name: {self.name}>"


class Rating(db.Model):
    """A restaurant rating"""

    __tablename__ = "rating"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    # pic = db.Column(db.Text)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text)
    yelp_id=db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    # restaurant_id = db.Column(db.Integer, db.ForeignKey("fav_rest.restaurant_id"), nullable=False)

    user = db.relationship("User", back_populates="ratings")
    # restaurant = db.relationship("Fav_rest", back_populates="ratings")

    def __repr__(self):
        """Show rating id and score"""

        return f"<rating_id: {self.rating_id} score: {self.score}>"


def connect_to_db(flask_app, db_uri="postgresql:///restaurant_guide", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)




