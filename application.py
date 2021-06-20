import logging

from flask import Flask

from blueprints.wunder import wunder
from blueprints.braze import braze
from blueprints.hellotracks import hellotracks

application = Flask(__name__)

logging.basicConfig(
    filename='log.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

application.register_blueprint(wunder, url_prefix="/wunder")
application.register_blueprint(hellotracks, url_prefix="/hellotracks")
application.register_blueprint(braze, url_prefix="/braze")

# TODO: Remove test routes
@application.route('/')
def hello_world():
    return 'It works!'


if __name__ == '__main__':
    application.run(host="0.0.0.0", debug=True)
