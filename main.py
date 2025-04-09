from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    name = "Wissam"
    return render_template('index.html', name=name)

@app.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("username or password wrong :((((")
        else:
            flash("Correct!!!!")

    return render_template("register.html")



if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)