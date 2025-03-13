from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/quiz_db"
mongo = PyMongo(app)

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# User Model
class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    if user:
        return User(user["_id"], user["username"])
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_pw = generate_password_hash(password)

        if mongo.db.users.find_one({"username": username}):
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        mongo.db.users.insert_one({"username": username, "password": hashed_pw})
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = mongo.db.users.find_one({"username": username})

        if user and check_password_hash(user["password"], password):
            login_user(User(user["_id"], user["username"]))
            flash("Login successful!", "success")
            return redirect(url_for("quiz"))

        flash("Invalid username or password", "danger")

    return render_template("login.html")

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if current_user.username != "admin":
        flash("Access denied!", "danger")
        return redirect(url_for("home"))

    if request.method == "POST":
        question = request.form["question"]
        options = [request.form["option1"], request.form["option2"], request.form["option3"], request.form["option4"]]
        correct_answer = request.form["correct_answer"]

        mongo.db.questions.insert_one({"question": question, "options": options, "correct_answer": correct_answer})
        flash("Question added successfully!", "success")

    questions = list(mongo.db.questions.find())
    return render_template("admin.html", questions=questions)

@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == "POST":
        answers = request.form.to_dict()
        score = 0
        questions = list(mongo.db.questions.find())

        for question in questions:
            q_id = str(question["_id"])
            if q_id in answers and answers[q_id] == question["correct_answer"]:
                score += 1

        mongo.db.scores.insert_one({"username": current_user.username, "score": score})
        flash(f"You scored {score}/{len(questions)}!", "success")
        return redirect(url_for("leaderboard"))

    questions = list(mongo.db.questions.find())
    random.shuffle(questions)
    return render_template("quiz.html", questions=questions[:5])

@app.route("/leaderboard")
def leaderboard():
    scores = list(mongo.db.scores.find().sort("score", -1))
    return render_template("leaderboard.html", scores=scores)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
