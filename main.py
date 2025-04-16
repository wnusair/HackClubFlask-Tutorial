from flask import Flask, render_template, request, flash
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret'

database_directory = 'data.csv'

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
            with open(database_directory, 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                print(csvfile)
                # wissam -> w, i, s, s, a, m
                csvwriter.writerow([username, password])
                


            flash("Correct!!!!")

    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        with open(database_directory, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            for row in csvreader:
                if row[0] and row[0] == [username,password]:
                    flash('Correct')
                else:
                    flash('Wrong username and/or password')
    
    return render_template('login.html')


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
