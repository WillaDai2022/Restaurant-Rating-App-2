RestaurantGuide enables users to search restaurants by zip code. Users can see the details of each restaurant as well as google map of it and can choose to review and favorite the restaurants they like. RestaurantGuide also recommends restaurants according to the location of the user.

## Table of Contents ☕️
* [About Me](#about-me)
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Installation](#installation)



## <a name="about-me"></a>About Me 👩🏻‍💻
Wei(Willa) Dai is a software engineer in Charlotte, NC. Find her on [LinkedIn](https://www.linkedin.com/in/wei-dai-willa/).

## <a name="tech-stack"></a>Tech Stack 🖥

**Backend**:  Python, Flask, PostgreSQL, SQLAlchemy <br/>
**Frontend**:  Jinja2, AJAX, Bootstrap, CSS, HTML, JavaScript, jQuery, Toastify JS<br/>
**APIs**:  Cloudinary, Google Maps JavaScript, Yelp

## <a name="features"></a>Features 🔎
Homepage and restaurant details page before user login in. No favorite button shown and no review can be left. Sign in and sign up button is shown.

![Before user login in](/static/image/gifs/status-before-login.gif)

Register for an account and login to use any app features. Regex is used to check the format of the phone number.

![Registration and Login](/static/image/gifs/register-login.gif)

Search for restaurants by zipcode.

![Restaurants Search](/static/image/gifs/search-rests.gif)

View a restaurant details and favourite a restaurant

![View Restaurant Details](/static/image/gifs/view-details.gif)

Write a review for a restaurant.

![Write restaurant Review](/static/image/gifs/write-review.gif)

User profile page and upload your own profile picture.

![Upload Profile Picture](/static/image/gifs/user-profile-page.gif)

View your favorited restaurants.

![View User Content](/static/image/gifs/view-favs-rests.gif)


## <a name="installation"></a>Set Up 🛠

* Install [Python](https://www.python.org/downloads/) <br/>
* Install [PostgreSQL](https://www.postgresql.org/download/)

Clone repository:
```
git clone https://github.com/WillaDai2022/Restaurant-Rating-App-2
```

Create and activate virtual environment:
```
virtualenv env
source env/bin/activate
```

Install the dependencies:
```
pip3 install -r requirements.txt
```
* Sign up to use the [Cloudinary API](https://cloudinary.com), [Google Maps Javascript API](https://developers.google.com/maps), [Yelp API](https://www.yelp.com/developers) and [Toastify JS API](https://apvarun.github.io/toastify-js/)

Save your Yelp and Cloudinary API keys to a file `secrets.sh`. The file should resemble this:
```
export YELP_KEY='***'
export CLOUDINARY_KEY='***'
export CLOUDINARY_SECRET='***'
```
Restrict your Google Maps key.

Source your keys:
```
source secrets.sh
```
Set up the database:
```
createdb restaurant_guide
psql restaurant_guide < restaurant_guide.sql
```

Run the app:
```
python3 server.py
```

* Go to 'localhost:5000' in your browser to view application locally.




