from flask import Flask,render_template,request

app = Flask(__name__)

def valid_login(param1, param2):
    param1=True
    param2=True

@app.route("/")
def get_main():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def receive_data():
    name = request.form['username']
    password = request.form['password']
    return render_template('login.html',username = name,
                           password = password)

if __name__ == "__main__":
    app.run(debug=True)