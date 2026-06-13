from flask import Flask, request, redirect, Response, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"  # Required for session management

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("Username: ")
        password = request.form.get("Password: ")

        if username == "admin" and password == "abc123":
            session["user"] = username
            return redirect(url_for("welcome"))
        
        else:
            return Response("Invalid credentials. Please try again.", mimetype="text/plain")
    
    return '''
    <h2>Login Page</h2>
    <form method="POST">
    Username : <input type="text" name="Username: "><br>
    Password : <input type="text" name="Password: "><br>
    <input type="submit" value="Login">
    </form>
'''
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
    
    '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

app.run(debug=True)