from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import AddCafe
from flask_bootstrap import Bootstrap5
from sqlalchemy import select
import random
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

class Base(DeclarativeBase):
    pass

Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///cafes.db")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)









class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# with app.app_context():
#     db.create_all()




@app.route("/")
def home():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return render_template("index.html", all_cafes=all_cafes)

@app.route("/add_cafe", methods=["GET", "POST"])
def add_cafe():
    form = AddCafe()
    if form.validate_on_submit():
        name = form.name.data
        map_url = form.map_url.data
        img_url = form.img_url.data
        location = form.location.data
        has_sockets = form.has_sockets.data
        has_toilet = form.has_toilet.data
        has_wifi = form.has_wifi.data
        can_take_calls = form.can_take_calls.data
        seats = form.seats.data
        coffee_price = form.coffee_price.data
        new_cafe = Cafe(
            name=name,
            map_url=map_url,
            img_url=img_url,
            location=location,
            seats=seats,
            has_sockets=has_sockets,
            has_wifi=has_wifi,
            has_toilet=has_toilet,
            can_take_calls=can_take_calls,
            coffee_price=coffee_price
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))



    return render_template("add_cafe.html", form=form)
@app.route("/delete/<int:cafe_id>")

def delete_post(cafe_id):
    post_to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
