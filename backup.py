from flask import Flask, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, UserVersion


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///noyo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "IT IS A SECRET!!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def root():
    """Homepage: redirect to /users."""

    return "Homepage"



##############################################################################
# user routes

# create new user
@app.route("/user", methods=["GET"])
def add_user_form():
    """Show form for adding new user."""
    return """
        <form method="post">
        <input name="firstname" type="text">
        <input name="middlename" type="text">
        <input name="lastname" type="text">
        <input name="email" type="text">
        <input name="age" type="number">
        <button>Submit</button>
        </form>
        """


@app.route("/user", methods=["POST"])
def add_user():
    """Handle user form:   
    """
    firstname= request.json["firstname"]
    middlename =request.json['middlename']
    lastname = request.json['lastname']
    email = request.json['email']
    age = request.json['age']
    version_id= 1
    try:
        new_user = User(firstname=firstname, middlename=middlename, lastname=lastname, email=email,age=age,version_id=version_id)
        db.session.add(new_user) 
        db.session.commit()
        response_json= jsonify(user=new_user.serialize_user())
        return (response_json, 201)
    except IntegrityError:
        return (jsonify("User already exists"), 400)
    
    

@app.route("/user/<int:user_id>")
def show_single_user(user_id):
    """Show single user."""

    single_user = User.query.get_or_404(user_id)
    return jsonify(user=single_user.serialize_user())
    


@app.route("/api/<int:version_id>/user/<int:user_id>")
def show_single_user_withversion(version_id, user_id):
    """Show detail on specific user with version id."""
    user = User.query.filter_by(id=user_id, version_id=version_id).first()

    if user is not None:
        return jsonify(user=user.serialize_user())
    
    else:
        user_prev_version = UserVersion.query.filter_by(user_id=user_id, version_id=version_id).first()
        if user_prev_version is not None:    
            return jsonify(user_prev_version.serialize_backup_user())    
        else:  
            return (jsonify(message="User not found with version id"))


@app.route("/users")
def show_all_users():
    """Show all users"""

    users_list = [user.serialize_user() for user in User.query.all()]
    return (jsonify(users=users_list), 200)


# update user with user id
@app.route("/user/<int:user_id>", methods=["PATCH"])
def update_single_user(user_id):
    """Update user with id"""
    user = User.query.get_or_404(user_id)        
    backup_user = UserVersion(user_id=user["id"], firstname= user["firstname"], middlename=user["middlename"],lastname=user["lastname"],email= user["email"],age=user["age"],version_id=user["version_id"])
    db.session.add(backup_user) 
    db.session.commit() 

    user = User.query.get_or_404(user_id)
    # db.session.query(User).filter_by(id=user_id).update(request.json)
    user.firstname = request.json.get('firstname',user.firstname)
    user.middlename = request.json.get('middlename',user.middlename)
    user.lastname = request.json.get('lastname', user.lastname)
    user.email = request.json.get('email', user.email)
    user.age = request.json.get('age', user.age)
    user.version_id = int(user.version_id) + 1    
    
    db.session.commit()
    return (jsonify(user=user.serialize_user()), 200)


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_single_user(user_id):
    """Delete user with id"""
    user = show_single_user(user_id)        
    backup_user = UserVersion(user_id=user["id"],
        firstname= user["firstname"],
        middlename=user["middlename"],
        lastname=user["lastname"],
        email= user["email"],
        age=user["age"],
        version_id=user["version_id"])

    db.session.add(backup_user) 
    db.session.commit() 
    
    delete_user = User.query.get_or_404(user_id)
    db.session.delete(delete_user) 
    db.session.commit()
    return jsonify(message="deleted")    
    
    








