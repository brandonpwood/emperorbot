import os

from flask import Flask
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)


app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
