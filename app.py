from flask import Flask, redirect, render_template, request, url_for
from config import Customer

app = Flask(__name__)


@app.route("/index")
def index():
    # customers = [
    #     Customer(name="Bob", age=79),
    #     Customer(name="Tom", age=57),
    #     Customer(name="Ken", age=73),
    # ]
    customers = Customer.select()
    return render_template("index.html", customers=customers)


@app.route("/add_customer", methods=["POST"])
def add():
    name = request.form["name"]
    age = int(request.form["age"])

    Customer.create(name=name, age=age)

    # return redirect("/index")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)


