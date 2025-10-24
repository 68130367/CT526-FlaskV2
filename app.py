from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


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


@app.route("/sum/<xx>/<yy>")
def sum_numbers(xx, yy):
    try:
        num1 = int(xx)
        num2 = int(yy)
        zz = num1 + num2

        result_message = f"The result of sum between {xx} and {yy} is {zz}"

        return render_template("sum.html", message=result_message)

    except ValueError:
        error_message = "You are using miss data type for operation"

        return render_template("sum.html", message=error_message)

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        return render_template("sum", message=error_message)


@app.route("/concat/<xx>/<yy>")
def concat_strings(xx, yy):
    result_concat = xx + yy
    result_message = f"The result of concat between {xx} and {yy} is {result_concat}"
    return render_template("sum.html", message=result_message)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
