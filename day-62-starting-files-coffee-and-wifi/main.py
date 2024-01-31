from flask import Flask, render_template
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location', validators=[DataRequired(), URL(message="invalid")])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    rating = SelectField('Coffee Rating',
                         choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                         validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating',
                       choices=["✘", "💪💪", "💪💪💪️", "💪💪💪💪", "💪💪💪💪💪"],
                       validators=[DataRequired()])
    power = SelectField('Power Socket Availability',
                        choices=["✘", "🔌🔌️", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_line = (str(form.cafe.data) + "," + str(form.location.data) + "," + str(form.open_time.data)
                     + "," + str(form.close_time.data) + "," + str(form.rating.data) + "," + str(form.wifi.data)
                     + "," + str(form.power.data))
        with open("cafe-data.csv", "a", encoding="utf-8") as file:
            file.write("\n" + cafe_line)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, row_length=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
