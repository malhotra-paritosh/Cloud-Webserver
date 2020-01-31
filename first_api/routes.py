from flask import render_template, flash
from first_api.forms import NumberInputForm
from first_api.models import Dummy_users
from first_api import app, db
from faker import Faker

fake = Faker()

@app.route('/', methods=['GET', 'POST']) # 'www.google.com/'
def home():
    form = NumberInputForm()
    if form.validate_on_submit():
        count = form.numberInput.data

        while(count>0):
            fk_name = fake.name()
            fk_email = fake.email()
            fk_add = fake.address()
            new_user = Dummy_users(userName=fk_name, email=fk_email, address=fk_add)
            db.session.add(new_user)
            db.session.commit()
            count=count-1
        flash(f'submitted', 'success')
    return render_template('home.html', form=form)
