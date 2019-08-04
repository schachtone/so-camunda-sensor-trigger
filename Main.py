import datetime
from flask import Flask
import connexion

#
# MMain class to simulate a machine in production
#


app = Flask(__name__)

# Creating the application instance
app = connexion.App(__name__, specification_dir='./')


# adding endpoint definitions based on swagger file
app.add_api('endpoints/swagger-actuator-endpoints.yml')

@app.route('/')
def index():
    return get_date_time_string()


def get_date_time_string():
    date = datetime.datetime.now()
    return str(date) + " - is up and running"


if __name__ == '__main__':
    app.run(debug=True)
