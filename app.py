from flask import Flask, render_template, redirect, request, session, url_for, flash
import pymongo
import bcrypt
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to store uploaded images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# MongoDB Connection
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client.wad_hw2
records = db.users

# Function to check allowed file extensions for profile pictures
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to create a new user in the database
def create_user(username, password, email, age):
    records.insert_one({
        "username": username,
        "password": password,
        "photo": "default",
        "city": "Not indicated",
        "profession": "Not indicated",
        "email": email,
        "age": age
    })

# Route for login page
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_record = records.find_one({"username": username})
        
        if user_record:
            user_password = user_record['password']
            if bcrypt.checkpw(password.encode('utf-8'), user_password):
                session['username'] = username
                session['photo'] = user_record['photo']
                return redirect(url_for("profile"))
            else:
                flash("Invalid password", "error")
        else:
            flash("Invalid username", "error")
        
        return redirect(url_for("login"))
    
    return render_template('login.html')

# Route for registration page
@app.route("/registration", methods=["GET", "POST"])
def registration_form():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        age = request.form.get("age")
        
        # Simple validation for email and age
        if not email or not age.isdigit():
            flash("Please provide a valid email and age", "error")
            return render_template('registration.html')

        user = records.find_one({'username': username})
        if user:
            flash("User with this username already exists. Please try again", "error")
            return render_template('registration.html')
        else:
            password = request.form.get("password")
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            create_user(username, hashed_password, email, int(age))
            flash("Account created! You can now log in", "success")
            return redirect(url_for("login"))
    
    return render_template('registration.html')

# Route for user profile page
@app.route('/profile', methods=['GET'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user = records.find_one({"username": username})
    
    if user:
        photo = user['photo']
        city = user['city']
        profession = user['profession']
        email = user['email']
        age = user['age']
        return render_template('profile.html', username=username, photo=photo, city=city, profession=profession, email=email, age=age)

# Route for changing password
@app.route('/changepasswd', methods=['POST'])
def changepasswd():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = records.find_one({"username": username})
    
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        
        if bcrypt.checkpw(old_password.encode('utf-8'), user['password']):
            hash_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            records.update_one({'username': username}, {'$set': {'password': hash_new_password}})
            flash("Password updated successfully", "success")
        else:
            flash("Incorrect old password", "error")
    
    return redirect(url_for("profile"))

# Route for updating user profile information
@app.route('/update', methods=['GET', 'POST'])
def updateInfo():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = records.find_one({"username": username})
    
    if request.method == 'POST':
        updates = {}
        city = request.form.get('city')
        if city:
            updates['city'] = city
        profession = request.form.get('profession')
        if profession:
            updates['profession'] = profession
        email = request.form.get('email')
        if email:
            updates['email'] = email
        age = request.form.get('age')
        if age:
            updates['age'] = int(age)

        # Handle profile picture upload
        if 'photo' in request.files:
            file = request.files['photo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                updates['photo'] = filepath

        if updates:
            records.update_one({'username': username}, {'$set': updates})
            flash("Information updated successfully!", "success")
        return redirect(url_for("profile"))
    
    return render_template('update_prof.html', photo=user['photo'], city=user['city'], profession=user['profession'], email=user['email'], age=user['age'])

# Route for logging out the user
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
