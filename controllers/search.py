from flask import *
from extensions import *
import requests
import json

search = Blueprint('search', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@search.route('/form')
def form_route():
    print("form route")
    

   
    return render_template("form.html")




