from flask import Flask, request, render_template_string, redirect, url_for
import os
from dotenv import dotenv_values

# Načítanie .env súboru
config = dotenv_values(".env")

app = Flask(__name__)

# Prihlasovacie údaje
USERNAME = config.get("USERNAME_APP")
PASSWORD = config.get("PASSWORD")

print(f"USERNAME: {USERNAME}")
print(f"PASSWORD: {PASSWORD}")

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

# Homepage s animáciou
homepage_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        #particles-js {
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: #282c34;
        }
        .content {
            position: relative;
            z-index: 1;
            text-align: center;
            color: white;
            font-family: Arial, sans-serif;
        }
        h1 {
            font-size: 4em;
            margin-top: 20%;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #61dafb;
            color: black;
            text-decoration: none;
            font-size: 1.2em;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    <div class="content">
        <h1>Welcome</h1>
        <a href="/app">Go to App</a>
    </div>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": {
                    "value": 80,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    },
                    "polygon": {
                        "nb_sides": 5
                    }
                },
                "opacity": {
                    "value": 0.5,
                    "random": false,
                    "anim": {
                        "enable": false,
                        "speed": 1,
                        "opacity_min": 0.1,
                        "sync": false
                    }
                },
                "size": {
                    "value": 3,
                    "random": true,
                    "anim": {
                        "enable": false,
                        "speed": 40,
                        "size_min": 0.1,
                        "sync": false
                    }
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 6,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false,
                    "attract": {
                        "enable": false,
                        "rotateX": 600,
                        "rotateY": 1200
                    }
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "repulse"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    },
                    "resize": true
                },
                "modes": {
                    "grab": {
                        "distance": 400,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "bubble": {
                        "distance": 400,
                        "size": 40,
                        "duration": 2,
                        "opacity": 8,
                        "speed": 3
                    },
                    "repulse": {
                        "distance": 200,
                        "duration": 0.4
                    },
                    "push": {
                        "particles_nb": 4
                    },
                    "remove": {
                        "particles_nb": 2
                    }
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("homepage"))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template_string(login_page)

@app.route("/homepage")
def homepage():
    return homepage_html

@app.route("/app")
def app_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>App</title>
    </head>
    <body>
        <h1>App Page</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)