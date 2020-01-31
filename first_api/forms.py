from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField
from wtforms.validators import DataRequired, NumberRange

class NumberInputForm(FlaskForm):
    numberInput = IntegerField('Enter Number', 
                                validators=[ DataRequired(), NumberRange(min=0, max=20000)])
    submit = SubmitField('Submit')