from flask import Flask, render_template
from flask_bootstrap import Bootstrap


application = Flask(__name__)
Bootstrap(application)


countryCount = [
    {
        'country': 'Germany',
        'count': 123,
        'recovered': 123
    }, {
        'country': 'India',
        'count': 1234,
        'recovered': 1234
    },
     {
        'country': 'France',
        'count': 12345,
        'recovered': 12345
    }
]


@application.route("/")
def overview():
    return render_template('overview.html', countries=countryCount)


@application.route('/about')
def about():
    return render_template('about.html')
