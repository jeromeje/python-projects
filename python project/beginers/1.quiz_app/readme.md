# **Quiz App (Flask + MongoDB) 🧠**

## **📌 Project Description**
The **Quiz App** is a web-based application built using **Flask and MongoDB**. It allows users to register, log in, take quizzes, and view leaderboard rankings. Admins can create and manage quiz questions.

---

## **📌 Features**
✅ **User Authentication** (Register/Login)  
✅ **Admin Panel** (Add/Delete Quiz Questions)  
✅ **Quiz Functionality** (Users can attempt quizzes)  
✅ **Leaderboard** (Ranks users based on their quiz scores)  
✅ **Secure Password Hashing**  

---

## **📌 Technologies Used**
- **Backend:** Flask, Flask-Login, Flask-PyMongo
- **Database:** MongoDB (Atlas/Local)
- **Frontend:** HTML, CSS, Bootstrap
- **Security:** Password Hashing (Werkzeug)

---

## **📌 Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone 
cd quiz-app-flask
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Start MongoDB**
Make sure MongoDB is running locally:
```sh
mongod --dbpath <your-db-path>
```

Or, use MongoDB Atlas (Cloud Database) and update the **MongoDB URI** in `app.py`:
```python
app.config["MONGO_URI"] = "your-mongodb-atlas-uri"
```

### **4️⃣ Run Flask App**
```sh
python app.py
```

### **5️⃣ Open in Browser**
Go to:  
👉 `http://127.0.0.1:5000`

---

## **📌 Usage**
### **🔹 User Features**
- **Register & Login**
- **Attempt a Quiz**
- **View Leaderboard**

### **🔹 Admin Features**
- **Login as "admin"**
- **Add Quiz Questions**
- **Manage Quiz Database**

---

## **📌 Project Structure**
```
/quiz-app
    ├── /templates
    │   ├── index.html
    │   ├── register.html
    │   ├── login.html
    │   ├── admin.html
    │   ├── quiz.html
    │   ├── leaderboard.html
    ├── /static
    │   ├── style.css
    ├── app.py
    ├── requirements.txt
    ├── README.md
```

---

## **📌 Screenshots**
### 🏠 Home Page  
![Home Page](https://via.placeholder.com/600x300.png?text=Home+Page)

### 🔐 Login Page  
![Login Page](https://via.placeholder.com/600x300.png?text=Login+Page)

### 📋 Quiz Page  
![Quiz Page](https://via.placeholder.com/600x300.png?text=Quiz+Page)

---

## **📌 Future Improvements 🚀**
✅ **Quiz Timer Feature**  
✅ **Multiple Quiz Categories**  
✅ **User Profile with Past Scores**  

---

## **📌 Contributing 🤝**
Want to improve this project? Feel free to contribute!  
1. Fork the repository  
2. Create a new branch (`feature-branch`)  
3. Commit your changes  
4. Open a Pull Request  

---

🔹 **Author:** 
🔹 **GitHub:** 

🚀 *Happy Coding!* 🎯