from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User, Rating, Fav_rest
import crud
from jinja2 import StrictUndefined
import requests
import json,os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route("/sign_in")
def sign_in():
    """User login page"""

    return render_template("sign-in.html")


@app.route("/all_rests", methods=["POST"])
def process_login():
    """Process user login and show 10 restaurants"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Unable to login with this email address and password. Check your login information and try again.")
        return redirect("/sign_in")
    else:
        # Log in user by storing the user's email and id in session
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        session["fname"] = user.fname
        session["lname"] = user.lname
        flash(f"Welcome back, {user.fname} {user.lname}!")
        return render_template("all-rests.html")


@app.route("/sign_up")
def sign_up():
    """User sign up page"""

    return render_template("sign-up.html")


@app.route("/sign_up", methods=["POST"])
def process_sign_up():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    phone = request.form.get("phone")


    user1 = crud.get_user_by_email(email)
    user2 = crud.get_user_by_phone(phone)

    if user1:
        flash("An account is already associated with this email. Sign in to get started.")
    elif user2:
        flash("Mobile number already exists. Please try again with another one")
    elif phone and len(phone) != 10:
        flash("Phone number is of invalid format")
    elif password and len(password) < 8:
        flash("Password must contain at least 8 characters.")
    else:
        new_user = crud.create_user(email, password, phone, fname, lname)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account was created successfully and you can now log in.")

    return redirect("/sign_up")


@app.route("/get_restaurants.json")
def get_rests_info():
    """Get restaurant info from Yelp API(default location Charlotte, NC 28226)"""

    location = request.args.get("location")

    if not location:
        location = "28226"

    #define the parameters
    parameters = {
        "term" : "restaurants",
        "radius": "5000",
        "limit": "10",
        "location": location
    }

    restaurants = yelp_api_get(None, "businesses/search", parameters).json()

    return restaurants

@app.route("/rest_details/<yelp_id>")
def show_restaurant_details(yelp_id):
    """Show details of a restaurant"""

    rest = yelp_api_get(yelp_id, "businesses", None).json()
   
    ratings = crud.get_rating_by_yelp_id(yelp_id)

    return render_template("rest-details.html", rest = rest, ratings=ratings, yelp_id=yelp_id)






# @app.route("/get_rest_review/<yelp_id>")
# def get_restaurant_reviews(yelp_id):
#     """Get reviews of a restaurant"""

#     ratings = Rating.query.filter(Rating.yelp_id == yelp_id).first()

#     if ratings:
#         return jsonify(ratings)
#     else:
#         return jsonify([])
        

@app.route("/review_page/<yelp_id>")
def leave_review(yelp_id):
    """User review edit page"""

    return render_template("review-page.html", yelp_id=yelp_id)


@app.route("/review_page/<yelp_id>", methods = ["POST"])
def save_user_review(yelp_id):
    """Save user review into database"""

    user_id = session.get("user_id")

    if user_id is None:
        flash("Please log in to leave a review")
        return redirect(f"/review_page/{yelp_id}")
    else:
        user = User.query.get(session["user_id"])
        title = request.form.get("title")
        score = int(request.form.get("score"))
        review = request.form.get("review")
        yelp_id = yelp_id

        rating = crud.create_rating_without_pic(user, title, score, review, yelp_id)
        db.session.add(rating)
        db.session.commit()
        return redirect(f"/rest_details/{yelp_id}")
        
@app.route("/sign_out")
def sign_out():
    """User Sign Out"""

    session.clear
    return redirect("/")

    
    

# Sending data from a form without javascript
# when user submits form, user's inputs will be sent to the route entered in the action attribute
# then you can get the data using request.form or request.get


## Sending data from a form, using javascript as middle man
#don't need action attribute
# you would use a js event listner, listening for submit event from form
#evt.preventdefault
# get the values using queryselector, save to a object (dictionary)
#then make fetch request using that object
# https://fellowship.hackbrightacademy.com/materials/serft11/lectures/ajax/#post-requests-frontend


#    



# @app.route("/")
# def show_all_movies():
#     """View all movies"""

#     movies = crud.get_movies()

#     return render_template("all_movies.html", movies = movies)


# @app.route("/movies/<movie_id>")
# def show_movie(movie_id):
#     """Show details on a particular movie."""

#     movie = crud.get_movie_by_id(movie_id)

#     return render_template("movie_details.html", movie=movie)


# @app.route("/users")
# def show_all_users():
#     """View all users"""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     """Show user details"""
    
#     user = crud.get_user_by_id(user_id)

#     return render_template("user_details.html", user = user)




# @app.route("/movies/<movie_id>/ratings", methods=["POST"])
# def create_rating(movie_id):
#     """Create a new rating for the movie."""

#     logged_in_email = session.get("user_email")
#     print(logged_in_email)
#     rating_score = request.form.get("rating")

#     if logged_in_email is None:
#         flash("You must log in to rate a movie.")
#     elif not rating_score:
#         flash("Error: you didn't select a score for your rating.")
#     else:
#         user = crud.get_user_by_email(logged_in_email)
#         movie = crud.get_movie_by_id(movie_id)

#         rating = crud.create_rating(user, movie, int(rating_score))
#         db.session.add(rating)
#         db.session.commit()

#         flash(f"You rated this movie {rating_score} out of 5.")

#     return redirect(f"/movies/{movie_id}")

def yelp_api_get(yelp_id, end_point, parameters):
    url = f"https://api.yelp.com/v3/{end_point}"
    yelp_key = os.environ.get("YELP_KEY")
    HEADERS = {"Authorization": "Bearer %s" % yelp_key}

    if yelp_id:
        return requests.get(f"{url}/{yelp_id}", headers=HEADERS)
    else:
        return requests.get(url, params=parameters, headers=HEADERS)


if __name__ == "__main__":
    # connect to database before app.run gets called. 
    # If not, Flask won’t be able to access your database
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
