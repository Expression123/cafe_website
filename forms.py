from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL
# from flask_ckeditor import CKEditorField

class AddCafe(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Map_Url", validators=[DataRequired(), URL()])
    img_url = StringField("Image Url", validators=[DataRequired(), URL()])
    location = StringField("What is the location", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets?",)
    has_toilet = BooleanField("Has Toilet?", )
    has_wifi = BooleanField("Has Wifi?", )
    can_take_calls = BooleanField("Can Take Calls?",)
    seats = StringField("Number Of Seats Cafe Has", validators=[DataRequired()])
    coffee_price = StringField("coffee_Price", validators=[DataRequired()])
    submit_field = SubmitField("Click To Add Cafe Info")
