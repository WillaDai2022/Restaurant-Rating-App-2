"""CRUD operations."""

from model import db, User, Rating, Fav_rest, connect_to_db


def create_user(email, password, phone, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, phone=phone, fname=fname, lname=lname)

    return user


def get_users():
    """Show all the users"""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user with a specific id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_phone(phone):
    """Return a user by phone number"""

    return User.query.filter(User.phone == phone).first()


def create_fav_rest(yelp_id, name, ratings, users):
    """Create and return a new restaurant."""

    restaurant = Fav_rest(
        yelp_id=yelp_id, 
        name=name, 
        ratings=ratings,
        users=users,
    )

    return restaurant


def get_reataurants():
    """Return all restaurants."""

    return Fav_rest.query.all()


def get_restaurant_by_id(restaurant_id):
    """Take a movie_id as an argument and return the movie with that ID."""

    return Fav_rest.query.get(restaurant_id)

def get_restaurant_by_yelp_id(yelp_id):
    "Take a yelp_id as an argument and return the movie with that ID."

    return Fav_rest.query.filter(Fav_rest.yelp_id==yelp_id)



def create_rating_without_pic(user, title, score, review, yelp_id):
    """create a rating to a movie by a user"""

    rating = Rating(user=user, title = title, 
                    score=score, review= review, yelp_id=yelp_id)
        
    return rating


def get_rating_by_yelp_id(yelp_id):
    """Return all the ratings for a specific restaurant"""

    return Rating.query.filter(Rating.yelp_id == yelp_id).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)