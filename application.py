import logging
import os

from flask import Flask

from blueprints.braze import braze
from blueprints.hellotracks import hellotracks
from blueprints.wunder import wunder
from blueprints.dixa import dixa

application = Flask(__name__)

logging.basicConfig(
    filename='log.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

application.register_blueprint(wunder, url_prefix="/wunder")
application.register_blueprint(hellotracks, url_prefix="/hellotracks")
application.register_blueprint(braze, url_prefix="/braze")
application.register_blueprint(dixa, url_prefix="/dixa")


if __name__ == '__main__':
    application.run(host="0.0.0.0")
