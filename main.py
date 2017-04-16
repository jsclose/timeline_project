from flask import *
from extensions import *

main = Blueprint('main', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@main.route('/', methods=['GET'])
def main_route():
   print("Running APP")

   return render_template("base.html")

