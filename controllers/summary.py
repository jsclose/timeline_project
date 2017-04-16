from flask import *
from extensions import *
import json, requests
import re
summary = Blueprint('summary', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@summary.route('/summary')
def summary_route():

	return render_template("summary.html")



	