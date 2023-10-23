from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///newflask.db"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/")
@app.route("/index")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/index")
        except:
            return "Error occured when post was created"

    else:
        return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
