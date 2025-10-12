from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/myid")
def my_id():
    student_id = "68130367"
    return render_template("myid.html", student_id=student_id)


@app.route("/tech")
def tech():
    return render_template("tech.html")


@app.route("/draw/<int:id>")
def draw(id):
    count = id
    star_pyramid = ["*" * i for i in range(1, id + 1)]
    return render_template("draw.html", count=id, stars=star_pyramid)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
