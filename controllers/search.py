from flask import *
from extensions import *
import requests
import json

search = Blueprint('search', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@search.route('/form', methods = ['POST', 'GET'])
def form_route():
    print("form route")
    event = request.args.to_dict()
    print (event)
    if event:
    	url = event['songid']
    	caption = event['caption']
    	credit = event['songname']
    	month = event['month']
    	day = event['day']
    	year = event['year']
    	headline = event['headline']
    	description = event['description']
    	cursor = db.cursor()
    	cursor.execute('INSERT into Timeline(year, month, day, headline, description, url, caption, credit) values( %s, %s, %s, %s, %s, %s, %s, %s)', (year, month, day, headline, description, url, caption, credit));

   
    return render_template("form.html")




