from flask import Flask, request, render_template_string, redirect, url_for
import os
from dotenv import load_dotenv

# Načítanie .env súboru
load_dotenv()

app = Flask(__name__)

# Prihlasovacie údaje
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Login stránka
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Hello World stránka
hello_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("hello"))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template_string(login_page)

@app.route("/hello")
def hello():
    return render_template_string(hello_page)

if __name__ == "__main__":
    app.run(debug=True)