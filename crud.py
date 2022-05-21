"""CRUD operations."""

from model import db, Account, Rating, Restaurant, connect_to_db


def create_account(email, password, phone, fname, lname):
    """Create and return a new user account."""

    account = Account(email=email, password=password, phone=phone, fname=fname, lname=lname, photo = f"/static/image/backgrounds/no-photo.png")

    return account


def get_accounts():
    """Show all the user accounts"""

    return Account.query.all()


def get_account_by_id(account_id):
    """Return a user account with a specific id"""

    return Account.query.get(account_id)


def get_account_by_email(email):
    """Return a user account by email."""

    return Account.query.filter(Account.email == email).first()


def get_account_by_phone(phone):
    """Return a user account by phone number"""

    return Account.query.filter(Account.phone == phone).first()


def create_rest(yelp_id, name, address, url, accounts):
    """Create and return a new restaurant."""

    restaurant = Restaurant(
        yelp_id=yelp_id, 
        name=name, 
        address = address,
        url = url,
        fav_accounts=[accounts],
    )

    return restaurant


def get_reataurants():
    """Return all restaurants."""

    return Restaurant.query.all()


def get_restaurant_by_id(restaurant_id):
    """Take a movie_id as an argument and return the movie with that ID."""

    return Restaurant.query.get(restaurant_id)

def get_restaurant_by_yelp_id(yelp_id):
    "Take a yelp_id as an argument and return the movie with that ID."

    return Restaurant.query.filter(Restaurant.yelp_id==yelp_id).first()


def create_rating_without_pic(account, title, score, review, yelp_id):
    """create a rating to a restaurant by a user"""

    rating = Rating(account=account, title = title, 
                    score=score, review= review, yelp_id=yelp_id)
        
    return rating


def create_rating_with_pic(account, title, score, review, yelp_id, pic):
    """Create a rating """

    rating = Rating(account=account, title = title, 
                    score=score, review= review, yelp_id=yelp_id, pic=pic)
        
    return rating


def get_rating_by_yelp_id(yelp_id):
    """Return all the ratings for a specific restaurant"""

    return Rating.query.filter(Rating.yelp_id == yelp_id).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)