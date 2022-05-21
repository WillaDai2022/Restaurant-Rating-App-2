"""Script to seed database."""

import os
import json
import crud
import model
import server

os.system("dropdb restaurant_guide")
os.system("createdb restaurant_guide")

model.connect_to_db(server.app)
model.db.create_all()

# Load user data from JSON file
with open("data/users.json") as f:
    user_data = json.loads(f.read())

# Create users, store them in list so we can use them
users_in_db = []
for user in user_data:
    password, email, phone, fname, lname = (
        user["password"],
        user["email"],
        user["phone"],
        user["fname"],
        user["lname"]
    )

    db_user = crud.create_account(email, password, phone, fname, lname)
    users_in_db.append(db_user)

# Add all users to database
model.db.session.add_all(users_in_db)
model.db.session.commit()

