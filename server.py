from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import requests
import json,os,re
import cloudinary.uploader

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

CLOUDINARY_KEY = os.environ["CLOUDINARY_KEY"]
CLOUDINARY_SECRET = os.environ["CLOUDINARY_SECRET"]
CLOUD_NAME = "djyfl2zja"

@app.route("/")
def homepage():
    """View homepage."""
    # if user is not logged in, sign-in and sign-up button will be shown
    # otherwise, hamburger icon is shown by clicking which user profile page and favorite 
    # restaurants page can be accessed

    return render_template("homepage.html")

@app.route("/sign_in")
def sign_in():
    """User login page"""

    return render_template("sign-in.html")


@app.route("/all_rests", methods=["POST"])
def process_login():
    """Process user login and show 20 restaurants"""

    
    # Grabbing entered in email and password
    email = request.form.get("email")
    password = request.form.get("password")

    # find user with the entered email in the database 
    user = crud.get_account_by_email(email)

    #if user doesn't exist or if password is not correct
    if not user or user.password != password:
        flash("Unable to login with this email address and password. Check your login information and try again.")
        return redirect("/sign_in")
    else:
        # Log in user by storing the user's info in session
        session["user_email"] = user.email
        session["user_id"] = user.account_id
        session["fname"] = user.fname
        session["lname"] = user.lname
        flash(f"Welcome back, {user.fname} {user.lname}!")
        
        # Default query string to YELP API
        parameters = {
            "term" : "restaurants",
            "radius": "5000",
            "limit": "20",
            "location": "28226"
        }

        # 20 rests' info 
        restaurants = yelp_api_get(None, "businesses/search", parameters).json()
        return render_template("all-rests.html", restaurants = restaurants)


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

    #regex 
    regex= r"(1[- ])?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}"

    user1 = crud.get_account_by_email(email)
    user2 = crud.get_account_by_phone(phone)

    if not fname:
        flash("First name is required")
    elif not lname:
        flash("Last name is required")
    elif not email:
        flash("Email is required")
    elif not phone:
        flash("Phone number is required")
    elif not password:
        flash("Password is required")
    elif user1:
        flash("An account is already associated with this email. Sign in to get started.")
    elif user2:
        flash("Mobile number already exists. Please try again with another one")
    elif not re.search(regex, phone):
        flash("Phone number is of invalid format")
    elif password and len(password) < 8:
        flash("Password must contain at least 8 characters")
    else:
        new_user = crud.create_account(email, password, phone, fname, lname)
        crud.db.session.add(new_user)
        crud.db.session.commit()
        flash("Your account was created successfully and you can now log in.")

    return redirect("/sign_up")


@app.route("/get_restaurants.json")
def get_rests_info():
    """Get restaurant info from Yelp API(default location Charlotte, NC 28226)"""

    location = request.args.get("location")

    print(location)

    if not location:
        location = "28226"

    #define the parameters
    parameters = {
        "term" : "restaurants",
        "radius": "5000",
        "limit": "20",
        "location": location
    }


    restaurants = yelp_api_get(None, "businesses/search", parameters).json()


    return restaurants

@app.route("/rest_details/<yelp_id>")
def show_restaurant_details(yelp_id):
    """Show details of a restaurant"""

    rest = yelp_api_get(yelp_id, "businesses", None).json()
   
    ratings = crud.get_rating_by_yelp_id(yelp_id)
    favorited = False
    if (session.get("user_id")):
        user = crud.get_account_by_id(session.get("user_id"))
        fav_rest = crud.get_restaurant_by_yelp_id(yelp_id)
   
        if fav_rest in user.fav_rests:
            favorited = True


    return render_template("rest-details.html", rest = rest, ratings=ratings, yelp_id=yelp_id, favorited=favorited)


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
        user = crud.get_account_by_id(session["user_id"])
        title = request.form.get("title")
        score = int(request.form.get("score"))
        review = request.form.get("review")
        yelp_id = yelp_id
        my_file = request.files['my-file']
        result = cloudinary.uploader.upload(my_file,
                                            api_key=CLOUDINARY_KEY,
                                            api_secret=CLOUDINARY_SECRET,
                                            cloud_name=CLOUD_NAME)

        if not result:
            rating = crud.create_rating_without_pic(user, title, score, review, yelp_id)
        else:
            img_url = result['secure_url']
            rating = crud.create_rating_with_pic(user, title, score, review, yelp_id, img_url)
        
        crud.db.session.add(rating)
        crud.db.session.commit()
        return redirect(f"/rest_details/{yelp_id}")
        

@app.route("/user_profile/<user_id>")
def show_user_profile(user_id):
    """show user profile"""


    user = crud.get_account_by_id(user_id)

  
    return render_template("user-profile.html", user=user, user_id = user_id)


@app.route("/user_photo_upload/<user_id>", methods=["POST"])
def upload_user_photo(user_id):
    """Process image uploaded by the user"""

    my_file = request.files["my-file"]

    result = cloudinary.uploader.upload(my_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name=CLOUD_NAME)
                                        
    img_url = result['secure_url']
    
    #get user by id and update the photo
    user = crud.get_account_by_id(user_id)
    user.photo = img_url
    session["photo"] = user.photo
    db.session.commit()

    return redirect(f"/user_profile/{user_id}")


@app.route("/user_fav_rests/<user_id>")
def show_user_fav_rest(user_id):
    """Show the restaurants favorited by one user"""

    user = crud.get_account_by_id(user_id)
    rests = user.fav_rests

    return render_template("user-fav-rests.html", rests = rests, user_id=user_id)


@app.route("/add_fav_rest", methods=["POST"])
def add_fav_rest():
    """Add user favorite restaurant"""

    user = crud.get_account_by_id(session.get("user_id"))
    name = request.json.get("name")
    address = request.json.get("address1") + " " + request.json.get("address2")
    url = request.json.get("url")
    yelp_id = request.json.get("yelp_id")


    rest = crud.get_restaurant_by_yelp_id(yelp_id) # Try to get restraunt
    
    if rest: # Check if the restruant already exists
        if not (user in rest.fav_accounts): # Check if the user has already favorited it
            # print("HI         ")
            rest.fav_accounts.append(user) # Add user to favorites. 
        else:
            return{"status": "Already favorited!"}
    else: # Create restraunt if it didn't exist
        
        rest = crud.create_rest(yelp_id, name, address, url, user)
        print(rest)
        crud.db.session.add(rest)
    
    crud.db.session.commit() # Update DB

    return {"status": "Favorite added!"}



@app.route("/delete_fav_rest", methods=["POST"])
def delete_fav_rest():

    user = crud.get_account_by_id(session.get("user_id"))
    status = ""

    yelp_id = request.json.get("yelp_id") #TODO 
    print(yelp_id)

    rest = crud.get_restaurant_by_yelp_id(yelp_id) # Try to get restraunt
    if rest: # if we get a restraurant back then
        rest.fav_accounts.remove(user)
        crud.db.session.commit()
        status = "success"
    else: # otherwise fail
        status = "fail"    

    return {"status": status}


  
@app.route("/sign_out")
def sign_out():
    """User Sign Out"""

    session.clear()
    
    return redirect("/")


def yelp_api_get(yelp_id, end_point, parameters):
    """Get restaurat(s) info frm Yelp API"""

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
